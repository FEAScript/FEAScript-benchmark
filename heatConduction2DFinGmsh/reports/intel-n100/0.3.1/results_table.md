| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.563 | 0.529 | 0.845 | 0.425 | 137 | 0.066 | 0.681 | 7.39e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.161 | 0.122 | 0.388 | 0.0665 | 72.9 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00748 | 0.00143 | 0.371 |  | 62.7 | 0.066 | 0.681 | 4.83e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00886 | 0.00143 | 0.368 |  | 63.9 | 0.066 | 0.681 | 6.25e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.4 | 0.066 | 0.681 | 4.26e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 1.28 | 1.2 | 1.51 | 1.12 | 160 | 0.0256 | 0.421 | 4.75e-12 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.334 | 0.219 | 0.553 | 0.23 | 78.9 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.0167 | 0.00354 | 0.378 |  | 64.4 | 0.0256 | 0.421 | 9.24e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.0245 | 0.00352 | 0.387 |  | 70.1 | 0.0256 | 0.421 | 1.65e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 31.6 | 0.0256 | 0.421 | 7.39e-13 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 28.9 | 28.6 | 29.2 | 27.9 | 714 | 0.00879 | 0.282 | 5.97e-11 | 1 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.708 | 0.432 | 0.937 | 0.758 | 97.3 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0627 | 0.0154 | 0.429 |  | 71.5 | 0.00879 | 0.282 | 1.34e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0871 | 0.0149 | 0.454 |  | 93.1 | 0.00879 | 0.282 | 1.92e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.03 | 0.01 | 2.08 |  | 36.8 | 0.00879 | 0.282 | 5.31e-12 | 5 |
| tri-linear-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 3.14 | 1.36 | 3.46 | 3.7 | 148 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.288 | 0.088 | 0.682 |  | 105 | 0.00268 | 0.153 | 4.89e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.399 | 0.0838 | 0.795 |  | 189 | 0.00268 | 0.153 | 4.55e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.17 | 0.07 | 2.27 |  | 60.9 | 0.00268 | 0.153 | 2.08e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 1.2 | 1.17 | 1.44 | 1.04 | 158 | 0.0185 | 0.482 | 9.19e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.287 | 0.23 | 0.507 | 0.211 | 83.2 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.0123 | 0.00376 | 0.367 |  | 63.9 | 0.0185 | 0.482 | 9.42e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.0152 | 0.0039 | 0.377 |  | 65.4 | 0.0185 | 0.482 | 9.29e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0.01 | 0 | 2.05 |  | 31.6 | 0.0185 | 0.482 | 1.34e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 28.1 | 28 | 28.4 | 27.7 | 579 | 0.00525 | 0.268 | 8.42e-11 | 1 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.584 | 0.456 | 0.818 | 0.66 | 104 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.039 | 0.0191 | 0.405 |  | 70.8 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0526 | 0.0181 | 0.415 |  | 78.1 | 0.00525 | 0.268 | 1.33e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 35.8 | 0.00525 | 0.268 | 2.5e-12 | 5 |
| tri-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 2.03 | 1.71 | 2.33 | 2.82 | 165 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.213 | 0.14 | 0.594 |  | 106 | 0.0014 | 0.142 | 1.94e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.264 | 0.135 | 0.647 |  | 131 | 0.0014 | 0.142 | 3.1e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.12 | 0.08 | 2.27 |  | 55.3 | 0.0014 | 0.142 | 1.05e-11 | 5 |
| tri-quadratic-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 12.5 | 10.5 | 12.9 | 27.4 | 550 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 1.38 | 1.09 | 1.82 |  | 263 | 0.000359 | 0.0728 | 1.15e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 1.65 | 1.05 | 2.1 |  | 371 | 0.000359 | 0.0728 | 1.51e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.77 | 0.59 | 3.31 |  | 142 | 0.000359 | 0.0728 | 1.62e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.365 | 0.348 | 0.593 | 0.337 | 133 | 0.12 | 1.74 | 6.25e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.174 | 0.14 | 0.398 | 0.105 | 73.3 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.0127 | 0.00208 | 0.371 |  | 63.2 | 0.12 | 1.74 | 3.13e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.018 | 0.00205 | 0.375 |  | 65.2 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.4 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.986 | 0.946 | 1.21 | 0.653 | 168 | 0.0355 | 0.82 | 6.85e-12 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.382 | 0.312 | 0.604 | 0.281 | 84.4 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0254 | 0.0067 | 0.386 |  | 65.4 | 0.0355 | 0.82 | 1.14e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0457 | 0.00661 | 0.405 |  | 74.5 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 2.07 |  | 32.2 | 0.0355 | 0.82 | 7.96e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 16.9 | 16.8 | 17.1 | 18 | 983 | 0.0104 | 0.396 | 1.09e-10 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.605 | 0.485 | 0.848 | 0.68 | 109 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0886 | 0.0342 | 0.458 |  | 76.9 | 0.0104 | 0.396 | 2.16e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.179 | 0.0331 | 0.544 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.04 | 0.02 | 2.09 |  | 38.2 | 0.0104 | 0.396 | 1.82e-12 | 5 |
| quad-linear-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 1.8 | 1.48 | 2.12 | 2.46 | 168 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.452 | 0.234 | 0.853 |  | 132 | 0.00296 | 0.191 | 6.45e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.826 | 0.229 | 1.23 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.17 | 0.1 | 2.3 |  | 67.5 | 0.00296 | 0.191 | 1.56e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 3.73 | 3.72 | 3.96 | 3.81 | 236 | 0.0142 | 0.364 | 2.42e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.329 | 0.283 | 0.554 | 0.255 | 86.2 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.0234 | 0.00659 | 0.38 |  | 65.4 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0338 | 0.0064 | 0.392 |  | 68.4 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 32.7 | 0.0142 | 0.364 | 1.96e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 145 | 145 | 145 | 168 | 1.33e+03 | 0.00365 | 0.177 | 2.23e-10 | 1 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.596 | 0.505 | 0.845 | 0.692 | 122 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0774 | 0.0397 | 0.443 |  | 78.4 | 0.00365 | 0.177 | 1.31e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.114 | 0.0376 | 0.481 |  | 90.5 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.04 | 0.02 | 2.13 |  | 40.1 | 0.00365 | 0.177 | 2.81e-12 | 5 |
| quad-quadratic-h0.1 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 2.01 | 1.83 | 2.3 | 2.8 | 241 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.395 | 0.288 | 0.779 |  | 140 | 0.000934 | 0.0872 | 7.77e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.568 | 0.276 | 0.957 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.15 | 0.09 | 2.42 |  | 68.8 | 0.000934 | 0.0872 | 1.34e-11 | 5 |
| quad-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 8.22 | 7.51 | 8.6 | 14.4 | 796 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 2.76 | 2.31 | 3.23 |  | 446 | 0.000235 | 0.0432 | 3.61e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 3.71 | 2.3 | 4.18 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.75 | 0.52 | 3.78 |  | 179 | 0.000235 | 0.0432 | 1.5e-11 | 5 |
