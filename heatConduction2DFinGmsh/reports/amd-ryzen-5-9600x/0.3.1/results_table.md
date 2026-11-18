| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.227 | 0.214 | 0.376 | 0.165 | 137 | 0.066 | 0.681 | 7.39e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.0614 | 0.0467 | 0.21 | 0.0449 | 72.1 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00328 | 0.000662 | 0.199 |  | 62.8 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00383 | 0.000651 | 0.205 |  | 64 | 0.066 | 0.681 | 6.25e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 0.422 |  | 29.2 | 0.066 | 0.681 | 4.26e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.462 | 0.428 | 0.598 | 0.377 | 159 | 0.0256 | 0.421 | 4.75e-12 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.141 | 0.0937 | 0.288 | 0.1 | 82.1 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.00772 | 0.00166 | 0.204 |  | 64.6 | 0.0256 | 0.421 | 9.66e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.00981 | 0.00162 | 0.207 |  | 70.4 | 0.0256 | 0.421 | 1.62e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0 | 0 | 0.464 |  | 30.4 | 0.0256 | 0.421 | 7.39e-13 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 12.8 | 12.7 | 12.9 | 13.2 | 804 | 0.00879 | 0.282 | 5.97e-11 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.308 | 0.201 | 0.487 | 0.326 | 97.6 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0298 | 0.00671 | 0.226 |  | 71.7 | 0.00879 | 0.282 | 1.31e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0349 | 0.00646 | 0.239 |  | 93.3 | 0.00879 | 0.282 | 1.85e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.01 | 0.01 | 0.443 |  | 35.7 | 0.00879 | 0.282 | 5.31e-12 | 5 |
| tri-linear-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 1.34 | 0.601 | 1.54 | 1.58 | 148 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.128 | 0.0354 | 0.326 |  | 105 | 0.00268 | 0.153 | 5e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.156 | 0.0348 | 0.404 |  | 189 | 0.00268 | 0.153 | 4.49e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.07 | 0.03 | 0.525 |  | 59.7 | 0.00268 | 0.153 | 2.08e-11 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.476 | 0.466 | 0.622 | 0.373 | 151 | 0.0185 | 0.482 | 9.19e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.129 | 0.105 | 0.26 | 0.102 | 82.7 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.00518 | 0.00171 | 0.199 |  | 64.1 | 0.0185 | 0.482 | 9.48e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.00642 | 0.00176 | 0.199 |  | 65.7 | 0.0185 | 0.482 | 9.34e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0 | 0 | 0.43 |  | 30.4 | 0.0185 | 0.482 | 1.34e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 12.6 | 12.6 | 12.8 | 14.6 | 624 | 0.00525 | 0.268 | 8.42e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.274 | 0.217 | 0.414 | 0.298 | 102 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.0163 | 0.00772 | 0.214 |  | 70.9 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0199 | 0.00767 | 0.216 |  | 78.2 | 0.00525 | 0.268 | 1.32e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.01 | 0.01 | 0.448 |  | 34.6 | 0.00525 | 0.268 | 2.5e-12 | 5 |
| tri-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 0.86 | 0.721 | 1 | 1.28 | 168 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.0796 | 0.0486 | 0.295 |  | 106 | 0.0014 | 0.142 | 1.88e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.0931 | 0.0475 | 0.307 |  | 131 | 0.0014 | 0.142 | 3.04e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.05 | 0.03 | 0.563 |  | 54.1 | 0.0014 | 0.142 | 1.05e-11 | 5 |
| tri-quadratic-h0.025 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 5.5 | 4.62 | 5.83 | 12.2 | 549 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 0.491 | 0.364 | 0.736 |  | 263 | 0.000359 | 0.0728 | 1.15e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 0.556 | 0.354 | 0.8 |  | 371 | 0.000359 | 0.0728 | 1.5e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.35 | 0.27 | 1.03 |  | 140 | 0.000359 | 0.0728 | 1.62e-11 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.18 | 0.172 | 0.332 | 0.131 | 134 | 0.12 | 1.74 | 6.25e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.0745 | 0.0601 | 0.215 | 0.0439 | 72.7 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.00485 | 0.000978 | 0.201 |  | 63.2 | 0.12 | 1.74 | 3.69e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.00962 | 0.00129 | 0.215 |  | 65.3 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 0.432 |  | 29.3 | 0.12 | 1.74 | 4.55e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.414 | 0.399 | 0.587 | 0.267 | 165 | 0.0355 | 0.82 | 6.85e-12 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.159 | 0.13 | 0.287 | 0.125 | 83.8 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0158 | 0.00452 | 0.222 |  | 65.4 | 0.0355 | 0.82 | 1.08e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0155 | 0.00316 | 0.212 |  | 74.8 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 31 | 0.0355 | 0.82 | 7.96e-13 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 5.96 | 5.92 | 6.11 | 6.86 | 986 | 0.0104 | 0.396 | 1.09e-10 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.267 | 0.216 | 0.428 | 0.313 | 109 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0372 | 0.0142 | 0.238 |  | 77.2 | 0.0104 | 0.396 | 2.05e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.0544 | 0.0149 | 0.256 |  | 110 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.02 | 0.01 | 0.462 |  | 36.9 | 0.0104 | 0.396 | 1.82e-12 | 5 |
| quad-linear-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 0.808 | 0.665 | 1 | 1.03 | 168 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.172 | 0.0811 | 0.393 |  | 132 | 0.00296 | 0.191 | 6.03e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.259 | 0.0785 | 0.492 |  | 258 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.08 | 0.04 | 0.575 |  | 66.3 | 0.00296 | 0.191 | 1.56e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 1.55 | 1.54 | 1.75 | 1.47 | 245 | 0.0142 | 0.364 | 2.42e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.142 | 0.123 | 0.271 | 0.127 | 86 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.00877 | 0.00297 | 0.204 |  | 65.7 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0121 | 0.00291 | 0.209 |  | 68.7 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0 | 0 | 0.465 |  | 31.3 | 0.0142 | 0.364 | 1.76e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 66.9 | 66.9 | 67.1 | 76.1 | 1.64e+03 | 0.00365 | 0.177 | 2.23e-10 | 1 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.259 | 0.22 | 0.403 | 0.288 | 126 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.0286 | 0.0151 | 0.227 |  | 78.5 | 0.00365 | 0.177 | 1.3e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.036 | 0.0145 | 0.238 |  | 90.6 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.01 | 0.01 | 0.488 |  | 38.7 | 0.00365 | 0.177 | 2.42e-12 | 5 |
| quad-quadratic-h0.1 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 0.885 | 0.804 | 1.06 | 1.31 | 240 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.138 | 0.0975 | 0.351 |  | 140 | 0.000934 | 0.0872 | 7.62e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.168 | 0.0929 | 0.382 |  | 185 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.06 | 0.04 | 0.611 |  | 67.4 | 0.000934 | 0.0872 | 1.03e-11 | 5 |
| quad-quadratic-h0.05 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 3.76 | 3.41 | 4.02 | 6.27 | 797 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 0.86 | 0.707 | 1.13 |  | 446 | 0.000235 | 0.0432 | 3.54e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 1.1 | 0.695 | 1.38 |  | 623 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.34 | 0.25 | 1.24 |  | 178 | 0.000235 | 0.0432 | 2.73e-11 | 5 |
