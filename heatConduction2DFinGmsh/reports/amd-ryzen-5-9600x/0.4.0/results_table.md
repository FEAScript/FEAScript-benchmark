| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.0333 | 0.023 | 0.133 | 0.0116 | 64.8 | 0.066 | 0.681 | 3.41e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.0561 | 0.0447 | 0.146 | 0.0336 | 65.8 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00315 | 0.000638 | 0.148 |  | 62.9 | 0.066 | 0.681 | 6.54e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.0037 | 0.000636 | 0.149 |  | 64.2 | 0.066 | 0.681 | 7.67e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 0.429 |  | 29.1 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.105 | 0.082 | 0.239 | 0.0628 | 70.4 | 0.0256 | 0.421 | 5.12e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.108 | 0.0851 | 0.249 | 0.074 | 74.6 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.00758 | 0.00164 | 0.197 |  | 64.6 | 0.0256 | 0.421 | 5.26e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.00965 | 0.00159 | 0.197 |  | 70.3 | 0.0256 | 0.421 | 1.18e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0 | 0 | 0.445 |  | 30.3 | 0.0256 | 0.421 | 1.17e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 0.19 | 0.15 | 0.354 | 0.0867 | 82.5 | 0.00879 | 0.282 | 2.33e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.203 | 0.166 | 0.335 | 0.22 | 97.4 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0278 | 0.00654 | 0.224 |  | 71.7 | 0.00879 | 0.282 | 2.19e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0344 | 0.00638 | 0.226 |  | 93.2 | 0.00879 | 0.282 | 3.27e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.02 | 0.01 | 0.451 |  | 35.6 | 0.00879 | 0.282 | 4.36e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript frontal | 0.498 | 0.412 | 0.704 | 0.441 | 132 | 0.00268 | 0.153 | 4.66e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 0.736 | 0.652 | 0.997 | 0.773 | 151 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.121 | 0.0313 | 0.325 |  | 105 | 0.00268 | 0.153 | 6.74e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.148 | 0.0306 | 0.353 |  | 189 | 0.00268 | 0.153 | 5.12e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.07 | 0.03 | 0.509 |  | 59.6 | 0.00268 | 0.153 | 2.26e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.0848 | 0.0729 | 0.212 | 0.0428 | 69 | 0.0185 | 0.482 | 1.59e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.109 | 0.0882 | 0.237 | 0.0743 | 66.8 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.0051 | 0.0017 | 0.198 |  | 64.1 | 0.0185 | 0.482 | 9.41e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.00606 | 0.00171 | 0.195 |  | 65.6 | 0.0185 | 0.482 | 9.27e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0 | 0 | 0.435 |  | 30.2 | 0.0185 | 0.482 | 2.02e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 0.144 | 0.123 | 0.273 | 0.0679 | 69.8 | 0.00525 | 0.268 | 1.68e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.207 | 0.18 | 0.338 | 0.194 | 90.5 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0161 | 0.00769 | 0.205 |  | 70.8 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0197 | 0.0075 | 0.211 |  | 78.2 | 0.00525 | 0.268 | 1.36e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.01 | 0.01 | 0.447 |  | 34.5 | 0.00525 | 0.268 | 2.05e-12 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript frontal | 0.32 | 0.282 | 0.454 | 0.266 | 102 | 0.0014 | 0.142 | 1.2e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 0.71 | 0.656 | 0.876 | 0.689 | 155 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.078 | 0.048 | 0.239 |  | 106 | 0.0014 | 0.142 | 2.37e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.0912 | 0.0466 | 0.291 |  | 131 | 0.0014 | 0.142 | 3.58e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.05 | 0.03 | 0.523 |  | 53.9 | 0.0014 | 0.142 | 4.58e-12 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript frontal | 3.16 | 3.06 | 3.41 | 2.99 | 307 | 0.000359 | 0.0728 | 1.18e-11 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 3.66 | 3.52 | 3.99 | 3.56 | 412 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 0.455 | 0.335 | 0.693 |  | 263 | 0.000359 | 0.0728 | 1.11e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 0.522 | 0.329 | 0.762 |  | 371 | 0.000359 | 0.0728 | 1.48e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.33 | 0.26 | 0.991 |  | 140 | 0.000359 | 0.0728 | 1.43e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.0745 | 0.0651 | 0.179 | 0.0249 | 69.5 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.0683 | 0.0539 | 0.159 | 0.0215 | 65.6 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.00479 | 0.000976 | 0.19 |  | 63.2 | 0.12 | 1.74 | 3.41e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.00637 | 0.000941 | 0.19 |  | 65.3 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 0.436 |  | 29.1 | 0.12 | 1.74 | 5.12e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.131 | 0.109 | 0.243 | 0.0508 | 71.6 | 0.0355 | 0.82 | 6.96e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.135 | 0.109 | 0.263 | 0.116 | 76.7 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0109 | 0.00311 | 0.208 |  | 65.4 | 0.0355 | 0.82 | 1.02e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0152 | 0.00309 | 0.203 |  | 74.6 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0 | 0 | 0.435 |  | 31 | 0.0355 | 0.82 | 5.54e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 0.202 | 0.169 | 0.352 | 0.101 | 82.8 | 0.0104 | 0.396 | 3.38e-12 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.253 | 0.215 | 0.403 | 0.258 | 100 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0365 | 0.0137 | 0.228 |  | 77.1 | 0.0104 | 0.396 | 2.73e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.0518 | 0.0135 | 0.246 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.02 | 0.01 | 0.45 |  | 36.7 | 0.0104 | 0.396 | 2.96e-12 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript frontal | 0.785 | 0.707 | 0.983 | 0.683 | 154 | 0.00296 | 0.191 | 1.12e-11 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 0.678 | 0.598 | 0.868 | 0.623 | 167 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.168 | 0.0792 | 0.343 |  | 132 | 0.00296 | 0.191 | 6.17e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.334 | 0.0874 | 0.624 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.13 | 0.07 | 0.785 |  | 66.2 | 0.00296 | 0.191 | 1.8e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 0.124 | 0.112 | 0.254 | 0.0531 | 71 | 0.0142 | 0.364 | 7.11e-13 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.127 | 0.104 | 0.236 | 0.0918 | 72.2 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.00868 | 0.00293 | 0.196 |  | 65.7 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.012 | 0.00283 | 0.2 |  | 68.7 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0 | 0 | 0.438 |  | 31.1 | 0.0142 | 0.364 | 1.04e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 0.216 | 0.195 | 0.349 | 0.0945 | 74.6 | 0.00365 | 0.177 | 2.98e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.238 | 0.207 | 0.366 | 0.218 | 105 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0282 | 0.0149 | 0.18 |  | 78.3 | 0.00365 | 0.177 | 1.29e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.036 | 0.0147 | 0.195 |  | 90.6 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.02 | 0.01 | 0.508 |  | 38.6 | 0.00365 | 0.177 | 2.27e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript frontal | 0.707 | 0.663 | 0.879 | 0.587 | 145 | 0.000934 | 0.0872 | 1.44e-11 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 0.694 | 0.633 | 0.87 | 0.675 | 198 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.132 | 0.092 | 0.336 |  | 140 | 0.000934 | 0.0872 | 7.93e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.167 | 0.092 | 0.388 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.11 | 0.07 | 0.936 |  | 67.2 | 0.000934 | 0.0872 | 9.99e-12 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript frontal | 7.12 | 7.02 | 7.39 | 6.8 | 473 | 0.000235 | 0.0432 | 1.44e-10 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 3.03 | 2.88 | 3.89 | 2.98 | 623 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 0.814 | 0.664 | 1.06 |  | 446 | 0.000235 | 0.0432 | 4.02e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 1.02 | 0.683 | 1.26 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.33 | 0.23 | 1.3 |  | 177 | 0.000235 | 0.0432 | 2.77e-11 | 5 |
