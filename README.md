# Absolute geolocation of SAR images: atmospheric (and tidal) effect

Assess the impact of atmospheric delay on the geolocation of satellite SAR images. This impact should be reflected on the overall offset between SAR images, and can be assessed by computing the dense offset time-series and comparing with the predicted delay from ionosphere and troposphere.

### Contents

1. range delay from SAR offset
   + config_cuDenseOffsets
   + offset_timeseries
   + prep_offset

2. range delay from atmosphere
   + prep_gim_tec
   + prep_igs_tec
   + prep_era5
   + tropo_ALOS2

3. comparison
   + atmos