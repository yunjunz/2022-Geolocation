## solid earth tide (SET) prediction

### Installation

```bash
# install fortran compiler from conda: gfortran_osx/linux-64
conda install gfortran_osx-64 

# generate Python interface from Fortran
f2py -c -m solid_f solid.f
```

### References:
+ Solid earth tide by Dennis Milbert: http://geodesyworld.github.io/SOFTS/solid.htm (access date: 6 Sep 2020)
   - Fortran: http://geodesyworld.github.io/SOFTS/solid.for.txt
   - C (translated by Joaquim Luis): https://github.com/GenericMappingTools/gmt/blob/master/src/geodesy/earthtide.c
