#!/usr/bin/env python3
# Author: Zhang Yunjun, Oct 2020


import os
import time
import glob
import pickle
import gdal
import numpy as np
from matplotlib import pyplot as plt, ticker, colors
from skimage.transform import resize
plt.rcParams.update({'font.size': 12})

from mintpy.utils import ptime, readfile, utils as ut


def save_gim_tec(out_file, date_list, gim_tec, top_tec, sub_tec, inc_angle, print_msg=True):
    # gather all into gim_tec dict
    tDict = {}
    tDict['date'] = np.array(date_list)
    tDict['time'] = np.array(ptime.date_list2vector(date_list)[0])
    tDict['TEC']    = gim_tec
    tDict['topTEC'] = top_tec
    tDict['subTEC'] = sub_tec

    ## calculate the predicted range delay
    band_freq = {
        'Lband' : 1.2575e9,   # ALOS-2, NISAR-L
        'Sband' : 3.2e9,      # NISAR-S
        'Cband' : 5.405e9,    # Sentinel-1
    }
    for band in band_freq.keys():
        freq = band_freq[band]
        for tec_type in ['TEC', 'subTEC', 'topTEC']:
            key = 'range_delay4{b}_{t}'.format(b=band, t=tec_type)
            if print_msg:
                print('calc {:<25} from {:<15}'.format(key, tec_type))

            off = ut.vtec2range_delay(tDict[tec_type], inc_angle, freq=freq)
            tDict[key] = off

    ## save to file
    os.makedirs(os.path.dirname(out_file), exist_ok=True)
    with open(out_file, 'wb') as f:
        pickle.dump(tDict, f)
        if print_msg:
            print('save data to file: {}'.format(out_file))

    return tDict



def read_offset_files(work_dir, fbaseDict={'SAR' : 'sar',
                                           'GIM' : 'TECgim',
                                           'IGS' : 'TECigs',
                                           'ERA' : 'era5',
                                           'SET' : 'set'}, print_msg=True):
    """Read the time-series offset from pickle files of all sources
    Parameters: work_dir  - str, path of working directory where pickle files store
                fbaseDict - dict, key and basename of pickle files
    Returns:    dDict     - dict, key and dataset in dict of time-series offset
                flag      - 1D np.ndarray marking the common elements
    """

    # output files from prep_*.ipynb
    dDict = {}
    for key, fbase in fbaseDict.items():
        fname = os.path.join(work_dir, '{}.pickle'.format(fbase))
        if os.path.isfile(fname):
            with open(fname, 'rb') as f:
                dDict[key] = pickle.load(f)
                if print_msg:
                    print('read {} data from pickle file: {}'.format(key, fname))

    # flag for common dates
    def get_common_index(t1s, t2s):
        """Get the flag matrix of the common elements between two input arrays
        Parameters: t1s   - 1D np.ndarray in size of (n1,)
                    t2s   - 1D np.ndarray in size of (n2,)
        Returns:    flag1 - 1D np.ndarray in size of (n1,)
                    flag2 - 1D np.ndarray in size of (n2,)
        """
        # get common dates
        tcomm = np.array(sorted(list(set(t1s) & set(t2s))))

        flag1 = np.zeros(t1s.size, dtype=np.bool_)
        for i in range(t1s.size):
            if t1s[i] in tcomm:
                flag1[i] = True

        flag2 = np.zeros(t2s.size, dtype=np.bool_)
        for i in range(t2s.size):
            if t2s[i] in tcomm:
                flag2[i] = True

        if not np.all(flag2):
            print('WARNING: the 1st does not have all dates in the 2nd dict!')

        return flag1, flag2

    if 'GIM' in dDict.keys():
        flag = get_common_index(dDict['SAR']['date'],
                                dDict['GIM']['date'])[0]
    else:
        flag = np.ones(len(dDict['SAR']['date']), dtype=np.bool_)

    return dDict, flag



