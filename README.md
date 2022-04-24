## Jupyter Notebooks for:

Yunjun, Z., Fattahi, H., Pi, X., Rosen, P., Simons, M., Agram, P., & Aoki, Y. (2022). Range Geolocation Accuracy of C/L-band SAR and its Implications for Operational Stack Coregistration. _IEEE Trans. Geosci. Remote Sens._, doi:[10.1109/TGRS.2022.3168509](https://doi.org/10.1109/TGRS.2022.3168509), [arXiv](https://doi.org/10.31223/X5F641).

### Data ([Zenodo](https://zenodo.org/record/6360749))

The used data in the paper is available on Zenodo at https://doi.org/10.5281/zenodo.6360749. It includes the following 3 test sites:

+ Sentinel-1 ascending track 149 in northern Chile
+ Sentinel-1 descending track 156 in northern Chile
+ ALOS-2 descending track 23 in southern Kyushu, Japan

For each dataset, it includes:

+ SAR range and azimuth offset stack (using ISCE-2/PyCuAmpcor)
+ SAR range offset time series (using MintPy)
+ JPL high resolution Global Ionospheric Maps (GIM) and the topside TEC for ChileSenAT149.
+ Solid Earth tides prediction (using PySolid)
+ ERA5 tropospheric delay prediction (using PyAPS)

### Figures

NOTE: This notebook is based on the released version of MintPy-1.3.3 and NOT maintained for furture development.

+ [Fig. 3](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_03_TS_tropo.ipynb) - Absolute tropospheric delay time series.
+ [Fig. 4](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_04_SET.ipynb) - Solid Earth tides in LOS direction and its power spectral density.
+ [Fig. 7](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_07_iono_delay.ipynb) - Ionospheric range delay as a function of the vertical TEC.
+ [Fig. 8](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_08_iono_refraction.ipynb) - Ionospheric range delay - Impact of refraction.
+ [Fig. 10](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_10_GIM_stats.ipynb) - Ionospheric range delay - Global distribution during the last half solar cycle.
+ [Fig. 11-13](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_11_13_TS_comp.ipynb) - Comparisons between the observed and predicted range delays for Sentinel-1 and ALOS-2.
+ [Fig. 14](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_14_S1AB_bias.ipynb) - Sentinel-1 A/B range bias.
+ [Fig. 15](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_15_stats_Tab_2_3.ipynb) - Distribution of the relative range geolocation error after routine geolocation error corrections.
+ [Fig. 16-17](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_16_17_topTEC.ipynb) - Topside TEC - Impact on range geolocation + Temporal variation of topside-total-TEC ratio.
+ [Fig. 18](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_18_GIM_scaling.ipynb) - Scaling the total TEC to the sub-orbital TEC - comparing different methods.
+ [Fig. 19](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_19_CDF.ipynb) - CDF (cumulative distribution function) of range mis-registration for Sentinel-1 and ALOS-2.
+ [Fig. 20](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Fig_20_coreg_demo.ipynb) - Demonstration of geometrical coregistration with model-driven refinements on ALOS over Hawaii.
+ [Table 4](https://nbviewer.org/github/yunjunz/2022-Geolocation/blob/main/notebooks/Tab_4_NISAR_budget.ipynb) - Range geolocation error budget for NISAR.
