| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.0823 | 0.0596 | 0.284 | 0.0305 | 65.1 | 0.066 | 0.681 | 3.41e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.148 | 0.123 | 0.345 | 0.043 | 66.4 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00749 | 0.00145 | 0.369 |  | 62.7 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00881 | 0.00143 | 0.364 |  | 64 | 0.066 | 0.681 | 7.67e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.4 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.257 | 0.206 | 0.463 | 0.149 | 71.5 | 0.0256 | 0.421 | 5.12e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.269 | 0.215 | 0.487 | 0.177 | 76.1 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.0168 | 0.00353 | 0.379 |  | 64.5 | 0.0256 | 0.421 | 4.83e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.0243 | 0.00346 | 0.382 |  | 70.1 | 0.0256 | 0.421 | 1.22e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 31.7 | 0.0256 | 0.421 | 1.17e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 0.432 | 0.355 | 0.701 | 0.199 | 83.1 | 0.00879 | 0.282 | 2.33e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.507 | 0.417 | 0.764 | 0.441 | 98.8 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0606 | 0.0153 | 0.425 |  | 71.5 | 0.00879 | 0.282 | 2.19e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0874 | 0.0149 | 0.453 |  | 93 | 0.00879 | 0.282 | 3.5e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.03 | 0.01 | 2.09 |  | 36.9 | 0.00879 | 0.282 | 4.36e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript frontal | 1.29 | 1.1 | 1.71 | 1.16 | 133 | 0.00268 | 0.153 | 4.66e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 1.5 | 1.31 | 1.9 | 1.34 | 150 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.288 | 0.0885 | 0.688 |  | 105 | 0.00268 | 0.153 | 6.54e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.398 | 0.0842 | 0.797 |  | 189 | 0.00268 | 0.153 | 4.92e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.16 | 0.07 | 2.29 |  | 61 | 0.00268 | 0.153 | 2.26e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.248 | 0.226 | 0.447 | 0.103 | 69.9 | 0.0185 | 0.482 | 1.59e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.266 | 0.215 | 0.468 | 0.163 | 68.4 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.0124 | 0.00382 | 0.372 |  | 63.9 | 0.0185 | 0.482 | 9.35e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.0148 | 0.00375 | 0.374 |  | 65.5 | 0.0185 | 0.482 | 9.22e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.6 | 0.0185 | 0.482 | 2.02e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 0.341 | 0.291 | 0.573 | 0.174 | 71.1 | 0.00525 | 0.268 | 1.68e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.501 | 0.433 | 0.73 | 0.439 | 87.1 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0387 | 0.0188 | 0.402 |  | 70.7 | 0.00525 | 0.268 | 1.23e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0538 | 0.0182 | 0.416 |  | 78.1 | 0.00525 | 0.268 | 1.37e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 35.9 | 0.00525 | 0.268 | 2.05e-12 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript frontal | 0.802 | 0.716 | 1.09 | 0.696 | 104 | 0.0014 | 0.142 | 1.2e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 1.71 | 1.58 | 1.99 | 1.63 | 155 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.216 | 0.142 | 0.594 |  | 106 | 0.0014 | 0.142 | 2.42e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.265 | 0.135 | 0.647 |  | 131 | 0.0014 | 0.142 | 3.66e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.12 | 0.08 | 2.27 |  | 55.3 | 0.0014 | 0.142 | 4.58e-12 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript frontal | 7.94 | 7.7 | 8.38 | 7.52 | 307 | 0.000359 | 0.0728 | 1.18e-11 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 8.9 | 8.59 | 9.4 | 8.91 | 428 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 1.38 | 1.09 | 1.83 |  | 263 | 0.000359 | 0.0728 | 1.12e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 1.67 | 1.06 | 2.12 |  | 371 | 0.000359 | 0.0728 | 1.48e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.76 | 0.59 | 3.31 |  | 142 | 0.000359 | 0.0728 | 1.43e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.175 | 0.157 | 0.4 | 0.0584 | 69.6 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.175 | 0.141 | 0.368 | 0.0658 | 65.8 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.0128 | 0.00209 | 0.372 |  | 63.1 | 0.12 | 1.74 | 2.84e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.018 | 0.00205 | 0.375 |  | 65.3 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.4 | 0.12 | 1.74 | 5.12e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.31 | 0.261 | 0.514 | 0.0992 | 72.3 | 0.0355 | 0.82 | 6.96e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.327 | 0.264 | 0.542 | 0.32 | 76.4 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0254 | 0.00677 | 0.385 |  | 65.3 | 0.0355 | 0.82 | 1.02e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0465 | 0.00666 | 0.409 |  | 74.5 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 32.3 | 0.0355 | 0.82 | 5.54e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 0.498 | 0.426 | 0.751 | 0.27 | 83.5 | 0.0104 | 0.396 | 3.38e-12 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.62 | 0.53 | 0.879 | 0.591 | 99.2 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0902 | 0.0342 | 0.458 |  | 76.9 | 0.0104 | 0.396 | 2.98e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.173 | 0.0325 | 0.543 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.04 | 0.02 | 2.09 |  | 38.2 | 0.0104 | 0.396 | 2.96e-12 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript frontal | 1.96 | 1.79 | 2.37 | 1.79 | 153 | 0.00296 | 0.191 | 1.12e-11 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 1.6 | 1.41 | 1.99 | 1.47 | 167 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.45 | 0.234 | 0.854 |  | 132 | 0.00296 | 0.191 | 6.74e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.815 | 0.226 | 1.22 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.17 | 0.1 | 2.29 |  | 67.4 | 0.00296 | 0.191 | 1.8e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 0.299 | 0.272 | 0.497 | 0.156 | 70.1 | 0.0142 | 0.364 | 7.11e-13 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.324 | 0.266 | 0.536 | 0.214 | 73 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.0235 | 0.00669 | 0.381 |  | 65.4 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0337 | 0.00648 | 0.396 |  | 68.5 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 32.7 | 0.0142 | 0.364 | 1.48e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 0.524 | 0.475 | 0.742 | 0.236 | 75.5 | 0.00365 | 0.177 | 2.98e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.589 | 0.51 | 0.839 | 0.519 | 107 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.076 | 0.0394 | 0.443 |  | 78.3 | 0.00365 | 0.177 | 1.3e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.113 | 0.0376 | 0.478 |  | 90.5 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.04 | 0.02 | 2.13 |  | 40.3 | 0.00365 | 0.177 | 3.3e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript frontal | 1.71 | 1.62 | 1.98 | 1.44 | 146 | 0.000934 | 0.0872 | 1.44e-11 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 1.68 | 1.52 | 1.99 | 1.61 | 198 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.395 | 0.287 | 0.785 |  | 140 | 0.000934 | 0.0872 | 7.96e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.573 | 0.278 | 0.963 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.15 | 0.09 | 2.41 |  | 68.8 | 0.000934 | 0.0872 | 1.24e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript frontal | 17.4 | 17.2 | 18.1 | 16.7 | 473 | 0.000235 | 0.0432 | 1.44e-10 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 7.16 | 6.79 | 7.71 | 7.13 | 624 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 3.17 | 2.65 | 3.7 |  | 446 | 0.000235 | 0.0432 | 4.13e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 4.32 | 2.56 | 4.95 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.8 | 0.53 | 3.81 |  | 179 | 0.000235 | 0.0432 | 1.54e-11 | 5 |
