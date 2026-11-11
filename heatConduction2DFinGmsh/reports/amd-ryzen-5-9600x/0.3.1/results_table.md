| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.214 | 0.203 | 0.357 | 0.156 | 137 | 0.066 | 0.681 | 7.39e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.0609 | 0.0466 | 0.2 | 0.0379 | 72.6 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00312 | 0.000642 | 0.193 |  | 62.8 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00367 | 0.000637 | 0.149 |  | 64 | 0.066 | 0.681 | 6.25e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 0.434 |  | 29.1 | 0.066 | 0.681 | 4.26e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.447 | 0.413 | 0.584 | 0.35 | 159 | 0.0256 | 0.421 | 4.75e-12 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.136 | 0.0903 | 0.272 | 0.0878 | 81.4 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.0076 | 0.00163 | 0.197 |  | 64.6 | 0.0256 | 0.421 | 9.66e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.00957 | 0.00159 | 0.199 |  | 70.3 | 0.0256 | 0.421 | 1.62e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0 | 0 | 0.436 |  | 30.3 | 0.0256 | 0.421 | 7.39e-13 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 11.3 | 11.2 | 11.5 | 11.4 | 801 | 0.00879 | 0.282 | 5.97e-11 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.283 | 0.182 | 0.426 | 0.305 | 97.6 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0276 | 0.00645 | 0.218 |  | 71.6 | 0.00879 | 0.282 | 1.31e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0346 | 0.00638 | 0.227 |  | 93.2 | 0.00879 | 0.282 | 1.85e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.02 | 0.01 | 0.493 |  | 35.6 | 0.00879 | 0.282 | 5.31e-12 | 5 |
| tri-linear-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 1.26 | 0.562 | 1.42 | 1.49 | 149 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.12 | 0.031 | 0.325 |  | 105 | 0.00268 | 0.153 | 5e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.148 | 0.0303 | 0.353 |  | 189 | 0.00268 | 0.153 | 4.49e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.07 | 0.03 | 0.548 |  | 59.6 | 0.00268 | 0.153 | 2.08e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.451 | 0.438 | 0.589 | 0.359 | 154 | 0.0185 | 0.482 | 9.19e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.117 | 0.0901 | 0.251 | 0.0894 | 83 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.00504 | 0.00169 | 0.197 |  | 64.1 | 0.0185 | 0.482 | 9.48e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.00607 | 0.0017 | 0.197 |  | 65.7 | 0.0185 | 0.482 | 9.34e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0 | 0 | 0.475 |  | 30.3 | 0.0185 | 0.482 | 1.34e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 11.2 | 11.2 | 11.4 | 12 | 623 | 0.00525 | 0.268 | 8.42e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.236 | 0.185 | 0.371 | 0.249 | 102 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.016 | 0.00766 | 0.205 |  | 70.8 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0197 | 0.00748 | 0.21 |  | 78.2 | 0.00525 | 0.268 | 1.32e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.01 | 0.01 | 0.496 |  | 34.5 | 0.00525 | 0.268 | 2.5e-12 | 5 |
| tri-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 0.803 | 0.671 | 0.961 | 1.12 | 167 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.0772 | 0.0478 | 0.277 |  | 106 | 0.0014 | 0.142 | 1.88e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.0906 | 0.0461 | 0.291 |  | 131 | 0.0014 | 0.142 | 3.04e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.05 | 0.03 | 0.549 |  | 54 | 0.0014 | 0.142 | 1.05e-11 | 5 |
| tri-quadratic-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 5.07 | 4.23 | 5.29 | 10.6 | 520 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 0.456 | 0.338 | 0.695 |  | 263 | 0.000359 | 0.0728 | 1.15e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 0.515 | 0.327 | 0.755 |  | 371 | 0.000359 | 0.0728 | 1.5e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.33 | 0.26 | 0.931 |  | 140 | 0.000359 | 0.0728 | 1.62e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.202 | 0.195 | 0.338 | 0.128 | 136 | 0.12 | 1.74 | 6.25e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.0715 | 0.0579 | 0.203 | 0.0411 | 73.2 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.0047 | 0.000953 | 0.197 |  | 63.1 | 0.12 | 1.74 | 3.69e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.00628 | 0.000932 | 0.196 |  | 65.2 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 29.2 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.389 | 0.374 | 0.526 | 0.248 | 164 | 0.0355 | 0.82 | 6.85e-12 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.148 | 0.12 | 0.286 | 0.136 | 85.3 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0106 | 0.00309 | 0.201 |  | 65.4 | 0.0355 | 0.82 | 1.08e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0151 | 0.00303 | 0.206 |  | 74.6 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 0.477 |  | 31 | 0.0355 | 0.82 | 7.96e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 5.48 | 5.44 | 5.66 | 6.16 | 989 | 0.0104 | 0.396 | 1.09e-10 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.248 | 0.199 | 0.394 | 0.283 | 108 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0366 | 0.0137 | 0.23 |  | 77.1 | 0.0104 | 0.396 | 2.05e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.0521 | 0.0135 | 0.246 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.02 | 0.01 | 0.497 |  | 36.8 | 0.0104 | 0.396 | 1.82e-12 | 5 |
| quad-linear-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 0.757 | 0.626 | 0.914 | 0.996 | 171 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.164 | 0.0768 | 0.375 |  | 132 | 0.00296 | 0.191 | 6.03e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.241 | 0.0739 | 0.453 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.07 | 0.04 | 0.558 |  | 66.2 | 0.00296 | 0.191 | 1.56e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 1.4 | 1.4 | 1.55 | 1.38 | 247 | 0.0142 | 0.364 | 2.42e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.135 | 0.116 | 0.269 | 0.102 | 87.4 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.00859 | 0.00293 | 0.199 |  | 65.6 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0117 | 0.00282 | 0.16 |  | 68.6 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0 | 0 | 0.48 |  | 31.1 | 0.0142 | 0.364 | 1.76e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 60.8 | 60.8 | 61 | 69 | 1.86e+03 | 0.00365 | 0.177 | 2.23e-10 | 1 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.248 | 0.207 | 0.403 | 0.274 | 125 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0283 | 0.0149 | 0.222 |  | 78.5 | 0.00365 | 0.177 | 1.3e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.0351 | 0.0144 | 0.229 |  | 90.6 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.01 | 0.01 | 0.498 |  | 38.7 | 0.00365 | 0.177 | 2.42e-12 | 5 |
| quad-quadratic-h0.1 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 0.854 | 0.778 | 0.978 | 1.16 | 239 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.132 | 0.092 | 0.298 |  | 140 | 0.000934 | 0.0872 | 7.62e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.162 | 0.0899 | 0.332 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.06 | 0.04 | 0.598 |  | 67.2 | 0.000934 | 0.0872 | 1.03e-11 | 5 |
| quad-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 3.5 | 3.18 | 3.75 | 5.57 | 797 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 0.81 | 0.664 | 1.07 |  | 446 | 0.000235 | 0.0432 | 3.54e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 0.987 | 0.661 | 1.24 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.33 | 0.24 | 1.14 |  | 177 | 0.000235 | 0.0432 | 2.73e-11 | 5 |
