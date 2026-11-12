| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.104 | 0.0608 | 0.3 | 0.0407 | 66 | 0.066 | 0.681 | 3.41e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.18 | 0.13 | 0.385 | 0.0655 | 65.9 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00743 | 0.00144 | 0.363 |  | 63.7 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00887 | 0.00144 | 0.373 |  | 65.1 | 0.066 | 0.681 | 7.67e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 2.05 |  | 30.7 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.346 | 0.222 | 0.547 | 0.145 | 72.6 | 0.0256 | 0.421 | 5.12e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.37 | 0.225 | 0.582 | 0.223 | 68.1 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.0179 | 0.00355 | 0.4 |  | 65.5 | 0.0256 | 0.421 | 4.83e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.0246 | 0.00349 | 0.39 |  | 71.2 | 0.0256 | 0.421 | 1.22e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 32 | 0.0256 | 0.421 | 1.17e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 0.643 | 0.354 | 0.854 | 0.394 | 80.4 | 0.00879 | 0.282 | 2.33e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.732 | 0.428 | 0.957 | 0.675 | 91.3 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0607 | 0.0153 | 0.425 |  | 72.5 | 0.00879 | 0.282 | 2.19e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0866 | 0.0149 | 0.454 |  | 94 | 0.00879 | 0.282 | 3.5e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.03 | 0.01 | 2.08 |  | 37.2 | 0.00879 | 0.282 | 4.36e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript frontal | 2.92 | 1.1 | 3.26 | 2.75 | 130 | 0.00268 | 0.153 | 4.66e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 3.43 | 1.41 | 3.72 | 3.4 | 139 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.285 | 0.0874 | 0.679 |  | 106 | 0.00268 | 0.153 | 6.54e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.397 | 0.084 | 0.794 |  | 190 | 0.00268 | 0.153 | 4.92e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.16 | 0.07 | 2.25 |  | 61.2 | 0.00268 | 0.153 | 2.26e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.306 | 0.264 | 0.497 | 0.122 | 70.3 | 0.0185 | 0.482 | 1.59e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.288 | 0.222 | 0.495 | 0.244 | 67.6 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.0154 | 0.00481 | 0.459 |  | 64.9 | 0.0185 | 0.482 | 9.35e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.0148 | 0.00373 | 0.383 |  | 66.5 | 0.0185 | 0.482 | 9.22e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 32 | 0.0185 | 0.482 | 2.02e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 0.419 | 0.297 | 0.626 | 0.221 | 70.2 | 0.00525 | 0.268 | 1.68e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.58 | 0.441 | 0.777 | 0.423 | 90.9 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0386 | 0.0188 | 0.4 |  | 71.6 | 0.00525 | 0.268 | 1.23e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0531 | 0.0181 | 0.415 |  | 79 | 0.00525 | 0.268 | 1.37e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 36.2 | 0.00525 | 0.268 | 2.05e-12 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript frontal | 1.03 | 0.718 | 1.27 | 0.845 | 102 | 0.0014 | 0.142 | 1.2e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 1.91 | 1.57 | 2.15 | 1.79 | 160 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.212 | 0.141 | 0.59 |  | 107 | 0.0014 | 0.142 | 2.42e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.265 | 0.135 | 0.646 |  | 132 | 0.0014 | 0.142 | 3.66e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.12 | 0.08 | 2.27 |  | 55.6 | 0.0014 | 0.142 | 4.58e-12 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript frontal | 9.38 | 7.55 | 9.81 | 8.97 | 305 | 0.000359 | 0.0728 | 1.18e-11 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 10.8 | 8.73 | 11.4 | 11.5 | 397 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 1.47 | 1.15 | 1.95 |  | 264 | 0.000359 | 0.0728 | 1.12e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 1.66 | 1.06 | 2.1 |  | 372 | 0.000359 | 0.0728 | 1.48e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.78 | 0.59 | 3.36 |  | 142 | 0.000359 | 0.0728 | 1.43e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.183 | 0.153 | 0.389 | 0.059 | 68.7 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.185 | 0.139 | 0.376 | 0.0813 | 65.6 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.0128 | 0.00208 | 0.376 |  | 64 | 0.12 | 1.74 | 2.84e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.0182 | 0.00207 | 0.386 |  | 66.4 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.8 | 0.12 | 1.74 | 5.12e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.306 | 0.224 | 0.502 | 0.145 | 71.3 | 0.0355 | 0.82 | 6.96e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.378 | 0.283 | 0.582 | 0.277 | 72.6 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0254 | 0.00672 | 0.382 |  | 66.3 | 0.0355 | 0.82 | 1.02e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0462 | 0.00661 | 0.407 |  | 75.5 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 32.6 | 0.0355 | 0.82 | 5.54e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 0.568 | 0.428 | 0.782 | 0.317 | 82.9 | 0.0104 | 0.396 | 3.38e-12 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.907 | 0.678 | 1.17 | 0.647 | 92.6 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0879 | 0.034 | 0.457 |  | 77.9 | 0.0104 | 0.396 | 2.98e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.179 | 0.0333 | 0.563 |  | 111 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.04 | 0.02 | 2.09 |  | 38.5 | 0.0104 | 0.396 | 2.96e-12 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript frontal | 2.17 | 1.82 | 2.49 | 1.9 | 150 | 0.00296 | 0.191 | 1.12e-11 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 1.88 | 1.52 | 2.21 | 2.03 | 154 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.45 | 0.234 | 0.852 |  | 133 | 0.00296 | 0.191 | 6.74e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.85 | 0.234 | 1.28 |  | 259 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.17 | 0.1 | 2.28 |  | 67.8 | 0.00296 | 0.191 | 1.8e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 0.342 | 0.306 | 0.53 | 0.137 | 72.5 | 0.0142 | 0.364 | 7.11e-13 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.348 | 0.281 | 0.552 | 0.213 | 68.7 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.0237 | 0.00666 | 0.388 |  | 66.4 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0337 | 0.00641 | 0.389 |  | 69.5 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 33 | 0.0142 | 0.364 | 1.48e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 0.518 | 0.436 | 0.724 | 0.243 | 73.4 | 0.00365 | 0.177 | 2.98e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.687 | 0.565 | 0.913 | 0.56 | 102 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0758 | 0.0393 | 0.44 |  | 79.2 | 0.00365 | 0.177 | 1.3e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.112 | 0.0378 | 0.476 |  | 91.4 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.04 | 0.02 | 2.12 |  | 40.5 | 0.00365 | 0.177 | 3.3e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript frontal | 1.82 | 1.66 | 2.11 | 1.74 | 130 | 0.000934 | 0.0872 | 1.44e-11 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 2.41 | 2.08 | 2.95 | 2.34 | 206 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.401 | 0.29 | 0.798 |  | 141 | 0.000934 | 0.0872 | 7.96e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.574 | 0.282 | 0.963 |  | 186 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.16 | 0.09 | 2.43 |  | 69.2 | 0.000934 | 0.0872 | 1.24e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript frontal | 18.1 | 17.7 | 18.7 | 17.9 | 473 | 0.000235 | 0.0432 | 1.44e-10 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 7.55 | 7.02 | 8.08 | 7.62 | 623 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 2.86 | 2.39 | 3.34 |  | 447 | 0.000235 | 0.0432 | 4.13e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 4.08 | 2.6 | 4.56 |  | 624 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.75 | 0.52 | 3.72 |  | 179 | 0.000235 | 0.0432 | 1.54e-11 | 5 |
