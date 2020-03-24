# offset4slow_motion

Measure slow tectonic deformation from the stack of azimuth dense offsets

## To do list

1. Try a co-seismic or co-eruptive deformation interferogram. 

   Find an earthquake here: https://www.usgs.gov/natural-hazards/earthquake-hazards/lists-maps-and-statistics

2. Update theoretical calculation of offset velocity for ALOS-2 and Sentinel-1. Demonstrate the need of CUDA code to support large memory usage, i.e. a window size of 1024 by 1024.

   If ALOS-2 could work, check PIXEL data portal for a suitable test area.
   
   Try a dry region for better coherence, use ALOS-2 for better coherence and higher azimuth resolution.
   

## Atmospheric impact on SAR geolocation (Fattahi et al., in prep.)

Assess the impact of atmospheric delay on the geolocation of satellite SAR images. This impact should be reflected on the overall offset between SAR images, and can be assessed by computing the dense offset time-series and comparing with the predicted delay from ionosphere and troposphere.

+ config_cuDenseOffsets
+ offset_timeseries
+ atmos

To do list:

+ check IPF version number for those data.

+ Summarize the offset difference on different sub-swaths from azimuth offset and on linear features from range offset, with Sentinel-1 A and B mark.

+ Time-series of the contribution from tide. There are software to get tide. Mark probably has one. We can discuss this alter
