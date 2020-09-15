#!/usr/bin/env python3
############################################################
# Program is part of MintPy                                #
# Copyright (c) 2013, Zhang Yunjun, Heresh Fattahi         #
# Author: Zhang Yunjun, Sep 2020                           #
############################################################
# Python wrapper for the solid earth tide calculation using solid.f.
# Fortran code is originally written by Dennis Milbert, 2018-06-01.
#   Available at: http://geodesyworld.github.io/SOFTS/solid.htm.
#   Modified by Simran Sangha and Zhang Yunjun in 2020-09-06
#   to calculate a spatial grid for a given date/time.
# Recomend import:
#   import solid


import os
import warnings
import numpy as np
from datetime import datetime as dt, timedelta
from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 12})

from mintpy.utils import ptime, readfile, writefile, utils as ut
from .solid_f import solid_f



def calc_solid_earth_tide(date_str, geom_file, display=False, print_msg=True):
    """Calculate solid earth tide (SET) in LOS direction.

    Parameters: date_str - str, date in YYYYMMDD format
                geom_file - str, path of geometry file in geo coordinates
    Returns:    tide_los/e/n/u - 2D np.ndarray, predicted solid earth tide in meters
    Examples:   geom_file = 'geo_geometryRadar.h5'
                tide_los = calc_solid_earth_tide('20200809', geom_file)[0]
    """
    atr = readfile.read_attribute(geom_file)

    # location and size
    lat0 = float(atr['Y_FIRST'])
    lon0 = float(atr['X_FIRST'])
    lat_step = float(atr['Y_STEP'])
    lon_step = float(atr['X_STEP'])
    length = int(atr['LENGTH'])
    width = int(atr['WIDTH'])

    # time
    utc_sec = float(atr['CENTER_LINE_UTC'])
    t = dt.strptime(date_str, '%Y%m%d') + timedelta(seconds=utc_sec)
    if print_msg:
        print('SOLID: calculate solid earth tide at {}'.format(t.isoformat()))

    # calc solid earth tide and write to text file
    txt_file = os.path.abspath('solid.txt')
    if os.path.isfile(txt_file):
        os.remove(txt_file)
    # Run twice to circumvent fortran bug which cuts off last file in loop
    solid_f(t.year, t.month, t.day, t.hour, t.minute, t.second, lat0-lat_step/2, lon0-lon_step/2, lat_step, lon_step, length-1, width-1)
    solid_f(t.year, t.month, t.day, t.hour, t.minute, t.second, lat0-lat_step/2, lon0-lon_step/2, lat_step, lon_step, length-1, width-1)
    if print_msg:
        print('SOLID: write data in ENU to file: {}'.format(txt_file))

    # read data from text file
    fc = np.loadtxt(txt_file, dtype=float, usecols=(2,3,4), delimiter=',', skiprows=7, max_rows=length*width)
    tide_n = fc[:, 0].reshape(length, width)
    tide_e = fc[:, 1].reshape(length, width)
    tide_u = fc[:, 2].reshape(length, width)

    # read LOS geometry
    if print_msg:
        print('SOLID: project data from ENU to radar line-of-sight direction')
    inc_angle = readfile.read(geom_file, datasetName='incidenceAngle')[0] * np.pi / 180.
    az_angle  = readfile.read(geom_file, datasetName='azimuthAngle')[0]
    head_angle = ut.azimuth2heading_angle(az_angle) * np.pi / 180.
    
    # get LOS unit vector
    with warnings.catch_warnings():
        warnings.simplefilter("ignore", category=RuntimeWarning)
        unit_vec = [
            np.sin(inc_angle) * np.cos(head_angle) * -1,
            np.sin(inc_angle) * np.sin(head_angle),
            np.cos(inc_angle),
        ]

    # convert ENU to LOS direction with positive towards satellite
    tide_los = (tide_e * unit_vec[0]
                + tide_n * unit_vec[1]
                + tide_u * unit_vec[2])

    # plot result
    if display:
        fig, axs = plt.subplots(nrows=2, ncols=2, figsize=[12, 5], sharex=True, sharey=True)
        for ax, data, fig_title in zip(axs.flatten(),
                                       [tide_e, tide_n, tide_u, tide_los],
                                       ['East', 'North', 'Up', 'LOS']):
            im = ax.imshow(data)
            ax.set_title(fig_title)
            fig.colorbar(im, ax=ax, label='m')
        fig.tight_layout()
        plt.show()

    return tide_los, tide_e, tide_n, tide_u


def get_solid_earth_tide_timeseries(date_list, geom_file, out_file=None, update_mode=True):
    """Get the time-series of solid earth tide.

    Parameters: date_list - list of str, dates in YYYYMMDD
                geom_file - str, path of geometry file in geo coordinates
                out_file  - str, output time-sereis file
    Returns:    out_file  - str, output time-sereis file
    """
    # default output filename
    if not out_file:
        out_fbase = 'SET.h5'
        if os.path.basename(geom_file).startswith('geo_'):
            out_fbase = 'geo_SET.h5'
        out_file = os.path.join(os.path.dirname(geom_file), out_fbase)

    if update_mode and os.path.isfile(out_file):
        print('update mode: ON')
        print('skip re-calculating and use existing file: {}'.format(out_file))
        return out_file

    # size info
    atr = readfile.read_attribute(geom_file)
    length = int(atr['LENGTH'])
    width = int(atr['WIDTH'])
    num_date = len(date_list)
    print('calculate solid earth tide for the following {} dates:\n{}'.format(num_date, date_list))

    ts_tide_los = np.zeros((num_date, length, width), dtype=np.float32)
    ts_tide_e = np.zeros((num_date, length, width), dtype=np.float32)
    ts_tide_n = np.zeros((num_date, length, width), dtype=np.float32)
    ts_tide_u = np.zeros((num_date, length, width), dtype=np.float32)

    # loop for calc
    print('calculating solid earth tide using solid.f (Dennis Milbert, Jun 2018) ...')
    prog_bar = ptime.progressBar(maxValue=num_date)
    for i in range(num_date):
        (ts_tide_los[i,:,:],
         ts_tide_e[i,:,:],
         ts_tide_n[i,:,:],
         ts_tide_u[i,:,:]) = calc_solid_earth_tide(date_list[i],
                                                   geom_file=geom_file,
                                                   display=False,
                                                   print_msg=False)
        prog_bar.update(i+1, suffix=date_list[i])
    prog_bar.close()

    ## output
    # attribute
    atr['FILE_TYPE'] = 'timeseries'
    atr['UNIT'] = 'm'
    for key in ['REF_Y', 'REF_X', 'REF_DATE']:
        if key in atr.keys():
            atr.pop(key)

    # dataset
    ds_dict = {}
    ds_dict['date']       = np.array(date_list, dtype=np.string_)
    ds_dict['timeseries'] = ts_tide_los
    ds_dict['east']       = ts_tide_e
    ds_dict['north']      = ts_tide_n
    ds_dict['up']         = ts_tide_u

    # write
    print('write to file: {}'.format(out_file))
    writefile.write(ds_dict, out_file=out_file, metadata=atr)

    return out_file

