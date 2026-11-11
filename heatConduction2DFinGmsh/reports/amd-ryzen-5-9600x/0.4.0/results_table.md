| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.0442 | 0.0232 | 0.191 | 0.0166 | 65.7 | 0.066 | 0.681 | 3.41e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.0693 | 0.0471 | 0.198 | 0.0246 | 66.2 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00316 | 0.000639 | 0.197 |  | 62.9 | 0.066 | 0.681 | 6.54e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00375 | 0.000642 | 0.197 |  | 64.1 | 0.066 | 0.681 | 7.67e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 0.461 |  | 29.2 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.136 | 0.083 | 0.255 | 0.0581 | 71.4 | 0.0256 | 0.421 | 5.12e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.132 | 0.0799 | 0.263 | 0.0905 | 68.1 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.00764 | 0.00164 | 0.198 |  | 64.7 | 0.0256 | 0.421 | 5.26e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.00963 | 0.0016 | 0.198 |  | 70.3 | 0.0256 | 0.421 | 1.18e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0 | 0 | 0.476 |  | 30.5 | 0.0256 | 0.421 | 1.17e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 0.245 | 0.125 | 0.378 | 0.164 | 82.1 | 0.00879 | 0.282 | 2.33e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.287 | 0.173 | 0.421 | 0.315 | 91.6 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0279 | 0.0065 | 0.22 |  | 71.7 | 0.00879 | 0.282 | 2.19e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0342 | 0.00633 | 0.228 |  | 93.3 | 0.00879 | 0.282 | 3.27e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.02 | 0.01 | 0.492 |  | 35.7 | 0.00879 | 0.282 | 4.36e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript frontal | 1.14 | 0.418 | 1.32 | 1.05 | 133 | 0.00268 | 0.153 | 4.66e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 1.27 | 0.553 | 1.45 | 1.52 | 143 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.122 | 0.0319 | 0.329 |  | 105 | 0.00268 | 0.153 | 6.74e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.151 | 0.0316 | 0.364 |  | 189 | 0.00268 | 0.153 | 5.12e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.07 | 0.03 | 0.549 |  | 59.7 | 0.00268 | 0.153 | 2.26e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.133 | 0.11 | 0.26 | 0.0488 | 70.4 | 0.0185 | 0.482 | 1.59e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.118 | 0.0866 | 0.248 | 0.0785 | 67.5 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.00521 | 0.00176 | 0.197 |  | 64.1 | 0.0185 | 0.482 | 9.41e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.00603 | 0.0017 | 0.197 |  | 65.7 | 0.0185 | 0.482 | 9.27e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0 | 0 | 0.476 |  | 30.4 | 0.0185 | 0.482 | 2.02e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 0.169 | 0.119 | 0.3 | 0.0814 | 70.6 | 0.00525 | 0.268 | 1.68e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.229 | 0.175 | 0.358 | 0.264 | 92.5 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0161 | 0.00769 | 0.166 |  | 70.9 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0195 | 0.00748 | 0.21 |  | 78.3 | 0.00525 | 0.268 | 1.36e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.01 | 0.01 | 0.488 |  | 34.6 | 0.00525 | 0.268 | 2.05e-12 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript frontal | 0.411 | 0.283 | 0.558 | 0.335 | 101 | 0.0014 | 0.142 | 1.2e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 0.803 | 0.669 | 0.952 | 1.18 | 150 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.0784 | 0.0485 | 0.281 |  | 106 | 0.0014 | 0.142 | 2.37e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.0941 | 0.048 | 0.293 |  | 131 | 0.0014 | 0.142 | 3.58e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.05 | 0.03 | 0.551 |  | 54 | 0.0014 | 0.142 | 4.58e-12 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript frontal | 3.77 | 3.02 | 3.97 | 3.6 | 305 | 0.000359 | 0.0728 | 1.18e-11 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 4.46 | 3.69 | 4.71 | 8.79 | 397 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 0.464 | 0.344 | 0.708 |  | 263 | 0.000359 | 0.0728 | 1.11e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 0.516 | 0.328 | 0.755 |  | 371 | 0.000359 | 0.0728 | 1.48e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.33 | 0.26 | 0.974 |  | 140 | 0.000359 | 0.0728 | 1.43e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.0681 | 0.0524 | 0.207 | 0.0248 | 68.4 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.0732 | 0.0544 | 0.198 | 0.0458 | 66.5 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.00473 | 0.000962 | 0.198 |  | 63.2 | 0.12 | 1.74 | 3.41e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.00644 | 0.000944 | 0.197 |  | 65.4 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 0.471 |  | 29.3 | 0.12 | 1.74 | 5.12e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.127 | 0.0884 | 0.254 | 0.0548 | 71 | 0.0355 | 0.82 | 6.96e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.146 | 0.107 | 0.279 | 0.146 | 71.3 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0106 | 0.0031 | 0.202 |  | 65.6 | 0.0355 | 0.82 | 1.02e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0151 | 0.00306 | 0.208 |  | 74.7 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 0.479 |  | 31 | 0.0355 | 0.82 | 5.54e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 0.233 | 0.174 | 0.372 | 0.121 | 83.5 | 0.0104 | 0.396 | 3.38e-12 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.269 | 0.213 | 0.411 | 0.312 | 96.5 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0367 | 0.0138 | 0.232 |  | 77.2 | 0.0104 | 0.396 | 2.73e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.0518 | 0.0135 | 0.249 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.02 | 0.01 | 0.492 |  | 37 | 0.0104 | 0.396 | 2.96e-12 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript frontal | 0.842 | 0.703 | 1.02 | 0.718 | 151 | 0.00296 | 0.191 | 1.12e-11 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 0.736 | 0.6 | 0.911 | 0.996 | 153 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.165 | 0.0775 | 0.375 |  | 132 | 0.00296 | 0.191 | 6.17e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.242 | 0.0746 | 0.452 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.07 | 0.04 | 0.564 |  | 66.4 | 0.00296 | 0.191 | 1.8e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 0.148 | 0.131 | 0.278 | 0.0512 | 71.6 | 0.0142 | 0.364 | 7.11e-13 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.127 | 0.0991 | 0.254 | 0.108 | 69.2 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.00864 | 0.00292 | 0.197 |  | 65.7 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0117 | 0.00284 | 0.202 |  | 68.7 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0 | 0 | 0.475 |  | 31.2 | 0.0142 | 0.364 | 1.04e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 0.219 | 0.181 | 0.356 | 0.102 | 73.9 | 0.00365 | 0.177 | 2.98e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.238 | 0.193 | 0.377 | 0.279 | 106 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0281 | 0.0149 | 0.221 |  | 78.5 | 0.00365 | 0.177 | 1.29e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.0355 | 0.0144 | 0.231 |  | 90.7 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.01 | 0.01 | 0.497 |  | 38.8 | 0.00365 | 0.177 | 2.27e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript frontal | 0.888 | 0.816 | 0.977 | 0.595 | 129 | 0.000934 | 0.0872 | 1.44e-11 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 0.746 | 0.662 | 0.898 | 0.976 | 206 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.132 | 0.0925 | 0.338 |  | 140 | 0.000934 | 0.0872 | 7.93e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.165 | 0.0912 | 0.372 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.06 | 0.04 | 0.598 |  | 67.4 | 0.000934 | 0.0872 | 9.99e-12 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript frontal | 7.12 | 6.94 | 7.36 | 6.78 | 473 | 0.000235 | 0.0432 | 1.44e-10 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 3.19 | 2.98 | 3.45 | 5.38 | 624 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 0.817 | 0.669 | 1.08 |  | 446 | 0.000235 | 0.0432 | 4.02e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 1.01 | 0.674 | 1.26 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.33 | 0.24 | 1.15 |  | 178 | 0.000235 | 0.0432 | 2.77e-11 | 5 |
