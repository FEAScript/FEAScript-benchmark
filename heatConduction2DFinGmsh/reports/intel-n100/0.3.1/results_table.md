| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.55 | 0.523 | 0.769 | 0.409 | 137 | 0.066 | 0.681 | 7.39e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.158 | 0.121 | 0.38 | 0.0744 | 72.9 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00744 | 0.00145 | 0.363 |  | 63.7 | 0.066 | 0.681 | 4.83e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.0088 | 0.00143 | 0.362 |  | 64.9 | 0.066 | 0.681 | 6.25e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.6 | 0.066 | 0.681 | 4.26e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 1.28 | 1.19 | 1.5 | 1.06 | 159 | 0.0256 | 0.421 | 4.75e-12 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.323 | 0.21 | 0.548 | 0.23 | 80.8 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.0167 | 0.00353 | 0.373 |  | 65.3 | 0.0256 | 0.421 | 9.24e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.0244 | 0.00351 | 0.38 |  | 71.2 | 0.0256 | 0.421 | 1.65e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.9 | 0.0256 | 0.421 | 7.39e-13 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 28.5 | 28.2 | 28.7 | 27.8 | 714 | 0.00879 | 0.282 | 5.97e-11 | 1 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.7 | 0.427 | 0.936 | 0.756 | 97.6 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0606 | 0.0152 | 0.423 |  | 72.3 | 0.00879 | 0.282 | 1.34e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0862 | 0.0147 | 0.45 |  | 94.1 | 0.00879 | 0.282 | 1.92e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.03 | 0.01 | 2.07 |  | 37.2 | 0.00879 | 0.282 | 5.31e-12 | 5 |
| tri-linear-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 3.09 | 1.35 | 3.42 | 3.66 | 149 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.285 | 0.0875 | 0.677 |  | 106 | 0.00268 | 0.153 | 4.89e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.393 | 0.0835 | 0.786 |  | 190 | 0.00268 | 0.153 | 4.55e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.16 | 0.07 | 2.26 |  | 61.1 | 0.00268 | 0.153 | 2.08e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 1.26 | 1.22 | 1.52 | 1.1 | 157 | 0.0185 | 0.482 | 9.19e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.423 | 0.321 | 0.716 | 0.221 | 83.4 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.0124 | 0.0038 | 0.375 |  | 64.8 | 0.0185 | 0.482 | 9.42e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.0147 | 0.00375 | 0.37 |  | 66.4 | 0.0185 | 0.482 | 9.29e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.8 | 0.0185 | 0.482 | 1.34e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 27.7 | 27.6 | 28 | 27.7 | 580 | 0.00525 | 0.268 | 8.42e-11 | 1 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.582 | 0.455 | 0.812 | 0.58 | 103 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0386 | 0.0188 | 0.397 |  | 71.7 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0529 | 0.018 | 0.412 |  | 79 | 0.00525 | 0.268 | 1.33e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 36.2 | 0.00525 | 0.268 | 2.5e-12 | 5 |
| tri-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 2.01 | 1.69 | 2.3 | 2.78 | 165 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.209 | 0.137 | 0.584 |  | 107 | 0.0014 | 0.142 | 1.94e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.262 | 0.133 | 0.64 |  | 132 | 0.0014 | 0.142 | 3.1e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.12 | 0.08 | 2.26 |  | 55.6 | 0.0014 | 0.142 | 1.05e-11 | 5 |
| tri-quadratic-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 12.4 | 10.4 | 12.9 | 27.2 | 550 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 1.37 | 1.08 | 1.82 |  | 264 | 0.000359 | 0.0728 | 1.15e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 1.64 | 1.05 | 2.09 |  | 372 | 0.000359 | 0.0728 | 1.51e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.76 | 0.58 | 3.3 |  | 142 | 0.000359 | 0.0728 | 1.62e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.367 | 0.351 | 0.589 | 0.338 | 134 | 0.12 | 1.74 | 6.25e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.182 | 0.147 | 0.401 | 0.11 | 73.1 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.0127 | 0.00208 | 0.366 |  | 64 | 0.12 | 1.74 | 3.13e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.0179 | 0.00203 | 0.372 |  | 66.1 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.7 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.993 | 0.953 | 1.22 | 0.636 | 165 | 0.0355 | 0.82 | 6.85e-12 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.372 | 0.304 | 0.59 | 0.261 | 84.4 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0254 | 0.00674 | 0.381 |  | 66.2 | 0.0355 | 0.82 | 1.14e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0459 | 0.00662 | 0.402 |  | 75.5 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 32.6 | 0.0355 | 0.82 | 7.96e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 16.7 | 16.6 | 17.1 | 17.7 | 987 | 0.0104 | 0.396 | 1.09e-10 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.613 | 0.489 | 0.848 | 0.671 | 111 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0881 | 0.034 | 0.453 |  | 77.8 | 0.0104 | 0.396 | 2.16e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.178 | 0.0326 | 0.544 |  | 111 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.04 | 0.02 | 2.09 |  | 38.3 | 0.0104 | 0.396 | 1.82e-12 | 5 |
| quad-linear-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 1.8 | 1.49 | 2.14 | 2.4 | 168 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.449 | 0.233 | 0.847 |  | 133 | 0.00296 | 0.191 | 6.45e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.819 | 0.225 | 1.22 |  | 259 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.17 | 0.1 | 2.28 |  | 67.7 | 0.00296 | 0.191 | 1.56e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 3.79 | 3.77 | 4.04 | 3.85 | 239 | 0.0142 | 0.364 | 2.42e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.327 | 0.28 | 0.55 | 0.251 | 85.9 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.0254 | 0.00704 | 0.418 |  | 66.4 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0364 | 0.00669 | 0.427 |  | 69.4 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 33 | 0.0142 | 0.364 | 1.96e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 154 | 153 | 154 | 160 | 1.33e+03 | 0.00365 | 0.177 | 2.23e-10 | 1 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.638 | 0.541 | 0.9 | 0.7 | 122 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0764 | 0.0395 | 0.48 |  | 79.3 | 0.00365 | 0.177 | 1.31e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.163 | 0.0523 | 0.686 |  | 91.4 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.04 | 0.02 | 2.13 |  | 40.5 | 0.00365 | 0.177 | 2.81e-12 | 5 |
| quad-quadratic-h0.1 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 2.06 | 1.86 | 2.35 | 2.91 | 240 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.409 | 0.293 | 0.805 |  | 141 | 0.000934 | 0.0872 | 7.77e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.584 | 0.283 | 0.983 |  | 186 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.15 | 0.09 | 2.41 |  | 69.1 | 0.000934 | 0.0872 | 1.34e-11 | 5 |
| quad-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 8.43 | 7.66 | 8.93 | 14.9 | 797 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 2.79 | 2.34 | 3.27 |  | 447 | 0.000235 | 0.0432 | 3.61e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 3.98 | 2.46 | 4.47 |  | 624 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.77 | 0.53 | 3.75 |  | 179 | 0.000235 | 0.0432 | 1.5e-11 | 5 |
