# offset4slow_motion

Measure slow tectonic deformation from the stack of azimuth dense offsets

## To do list

1. Try a co-seismic or co-eruptive deformation interferogram. 

   Find an earthquake here: https://www.usgs.gov/natural-hazards/earthquake-hazards/lists-maps-and-statistics

2. Update theoretical calculation of offset velocity for ALOS-2 and Sentinel-1. Demonstrate the need of CUDA code to support large memory usage, i.e. a window size of 1024 by 1024.

   If ALOS-2 could work, check PIXEL data portal for a suitable test area.
   
   Try a dry region for better coherence, use ALOS-2 for better coherence and higher azimuth resolution.
   

## For Fattahi et al. (in prep)

Note: please download the repository to see the embeded images.

1. [Offset stack](offset_stack.ipynb) from ISCE/topsStack

2. [Offset time-series](offset_timeseries.ipynb) from MintPy

To do list:

+ Get screenshots of different configurations on cuDenseOffsets.py, talk to Minyan, to make sure it's appropriate.

+ check IPF version number for those data.

+ Summarize the offset difference on different sub-swaths from azimuth offset and on linear features from range offset, with Sentinel-1 A and B mark.

+ try the Sentinel-1 asc track 149 data on Chile (ascending on low geomagnetic latitude with strong iono) from Liang et al. (2019, TGRS).


+ abs iono delay in meter and TECU

+ abs tropo delay in dry and wet

+ 


