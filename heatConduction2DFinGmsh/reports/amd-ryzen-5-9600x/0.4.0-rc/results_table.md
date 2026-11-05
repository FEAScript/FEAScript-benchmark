| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| tri-linear-h0.2 | 274 | FEAScript frontal | 0.0457 | 0.0214 | 0.139 | 0.0121 | 65.3 | 0.066 | 0.681 | 2.56e-13 | 5 |
| tri-linear-h0.2 | 274 | FEAScript sparse LU | 0.067 | 0.0478 | 0.155 | 0.0351 | 65.6 | 0.066 | 0.681 | 0 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem SuperLU | 0.00332 | 0.000678 | 0.16 |  | 65.8 | 0.066 | 0.681 | 5.4e-13 | 5 |
| tri-linear-h0.2 | 274 | scikit-fem fine integration | 0.00387 | 0.000661 | 0.16 |  | 67.1 | 0.066 | 0.681 | 6.25e-13 | 5 |
| tri-linear-h0.2 | 274 | Elmer UMFPACK | 0 | 0 | 0.421 |  | 29 | 0.066 | 0.681 | 4.99e-06 | 5 |
| tri-linear-h0.1 | 995 | FEAScript frontal | 0.129 | 0.0721 | 0.227 | 0.0609 | 70.8 | 0.0256 | 0.421 | 9.66e-13 | 5 |
| tri-linear-h0.1 | 995 | FEAScript sparse LU | 0.139 | 0.0841 | 0.234 | 0.0963 | 67.4 | 0.0256 | 0.421 | 0 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem SuperLU | 0.00761 | 0.00162 | 0.157 |  | 67.6 | 0.0256 | 0.421 | 9.66e-13 | 5 |
| tri-linear-h0.1 | 995 | scikit-fem fine integration | 0.00967 | 0.00159 | 0.158 |  | 73 | 0.0256 | 0.421 | 1.62e-12 | 5 |
| tri-linear-h0.1 | 995 | Elmer UMFPACK | 0 | 0 | 0.444 |  | 30.3 | 0.0256 | 0.421 | 4.99e-06 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript frontal | 0.258 | 0.14 | 0.39 | 0.165 | 80.5 | 0.00879 | 0.282 | 1.93e-12 | 5 |
| tri-linear-h0.05 | 3818 | FEAScript sparse LU | 0.297 | 0.182 | 0.426 | 0.321 | 89.5 | 0.00879 | 0.282 | 0 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem SuperLU | 0.0275 | 0.00649 | 0.22 |  | 74.4 | 0.00879 | 0.282 | 1.31e-12 | 5 |
| tri-linear-h0.05 | 3818 | scikit-fem fine integration | 0.0342 | 0.00631 | 0.226 |  | 96 | 0.00879 | 0.282 | 1.85e-12 | 5 |
| tri-linear-h0.05 | 3818 | Elmer UMFPACK | 0.02 | 0.01 | 0.493 |  | 35.6 | 0.00879 | 0.282 | 5e-06 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript frontal | 1.14 | 0.422 | 1.32 | 1.04 | 130 | 0.00268 | 0.153 | 3.61e-12 | 5 |
| tri-linear-h0.025 | 15092 | FEAScript sparse LU | 1.26 | 0.552 | 1.43 | 1.51 | 141 | 0.00268 | 0.153 | 0 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem SuperLU | 0.12 | 0.0312 | 0.327 |  | 108 | 0.00268 | 0.153 | 5e-12 | 5 |
| tri-linear-h0.025 | 15092 | scikit-fem fine integration | 0.149 | 0.0306 | 0.356 |  | 192 | 0.00268 | 0.153 | 4.49e-12 | 5 |
| tri-linear-h0.025 | 15092 | Elmer UMFPACK | 0.07 | 0.03 | 0.511 |  | 59.5 | 0.00268 | 0.153 | 5e-06 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript frontal | 0.0926 | 0.0727 | 0.18 | 0.0493 | 69.1 | 0.0185 | 0.482 | 8.67e-13 | 5 |
| tri-quadratic-h0.2 | 1033 | FEAScript sparse LU | 0.109 | 0.0815 | 0.237 | 0.086 | 67.5 | 0.0185 | 0.482 | 0 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem SuperLU | 0.00509 | 0.0017 | 0.194 |  | 67 | 0.0185 | 0.482 | 9.48e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | scikit-fem fine integration | 0.00609 | 0.0017 | 0.199 |  | 68.6 | 0.0185 | 0.482 | 9.34e-12 | 5 |
| tri-quadratic-h0.2 | 1033 | Elmer UMFPACK | 0 | 0 | 0.477 |  | 30.2 | 0.0185 | 0.482 | 4.99e-06 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript frontal | 0.173 | 0.121 | 0.302 | 0.0758 | 70.4 | 0.00525 | 0.268 | 2.19e-12 | 5 |
| tri-quadratic-h0.1 | 3857 | FEAScript sparse LU | 0.246 | 0.193 | 0.379 | 0.271 | 90.2 | 0.00525 | 0.268 | 0 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem SuperLU | 0.016 | 0.00767 | 0.206 |  | 73.5 | 0.00525 | 0.268 | 1.22e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | scikit-fem fine integration | 0.0196 | 0.0075 | 0.171 |  | 80.9 | 0.00525 | 0.268 | 1.32e-11 | 5 |
| tri-quadratic-h0.1 | 3857 | Elmer UMFPACK | 0.01 | 0.01 | 0.448 |  | 34.5 | 0.00525 | 0.268 | 5e-06 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript frontal | 0.414 | 0.285 | 0.558 | 0.341 | 101 | 0.0014 | 0.142 | 8.04e-12 | 5 |
| tri-quadratic-h0.05 | 15029 | FEAScript sparse LU | 0.795 | 0.664 | 0.943 | 1.13 | 139 | 0.0014 | 0.142 | 0 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem SuperLU | 0.0777 | 0.0479 | 0.279 |  | 109 | 0.0014 | 0.142 | 1.88e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | scikit-fem fine integration | 0.0907 | 0.0463 | 0.292 |  | 134 | 0.0014 | 0.142 | 3.04e-11 | 5 |
| tri-quadratic-h0.05 | 15029 | Elmer UMFPACK | 0.05 | 0.03 | 0.552 |  | 53.9 | 0.0014 | 0.142 | 5e-06 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript frontal | 3.76 | 3.03 | 3.96 | 3.55 | 305 | 0.000359 | 0.0728 | 1.59e-11 | 5 |
| tri-quadratic-h0.025 | 59885 | FEAScript sparse LU | 4.81 | 4.06 | 5.02 | 13.1 | 398 | 0.000359 | 0.0728 | 0 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem SuperLU | 0.451 | 0.333 | 0.689 |  | 266 | 0.000359 | 0.0728 | 1.15e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | scikit-fem fine integration | 0.511 | 0.323 | 0.748 |  | 374 | 0.000359 | 0.0728 | 1.5e-10 | 5 |
| tri-quadratic-h0.025 | 59885 | Elmer UMFPACK | 0.32 | 0.25 | 0.962 |  | 140 | 0.000359 | 0.0728 | 5e-06 | 5 |
| quad-linear-h0.4 | 415 | FEAScript frontal | 0.0627 | 0.0478 | 0.199 | 0.0278 | 67.5 | 0.12 | 1.74 | 3.69e-13 | 5 |
| quad-linear-h0.4 | 415 | FEAScript sparse LU | 0.0724 | 0.0554 | 0.195 | 0.0302 | 65.4 | 0.12 | 1.74 | 0 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem SuperLU | 0.00465 | 0.000946 | 0.197 |  | 66.2 | 0.12 | 1.74 | 3.69e-13 | 5 |
| quad-linear-h0.4 | 415 | scikit-fem fine integration | 0.00625 | 0.000928 | 0.199 |  | 68.1 | 0.117 | 1.7 | 0.0417 | 5 |
| quad-linear-h0.4 | 415 | Elmer UMFPACK | 0 | 0 | 0.469 |  | 29.1 | 0.12 | 1.74 | 4.99e-06 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript frontal | 0.122 | 0.09 | 0.247 | 0.0602 | 70.6 | 0.0355 | 0.82 | 8.53e-13 | 5 |
| quad-linear-h0.2 | 1519 | FEAScript sparse LU | 0.146 | 0.116 | 0.274 | 0.135 | 75.2 | 0.0355 | 0.82 | 0 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem SuperLU | 0.0104 | 0.00308 | 0.197 |  | 68.1 | 0.0355 | 0.82 | 1.08e-12 | 5 |
| quad-linear-h0.2 | 1519 | scikit-fem fine integration | 0.0149 | 0.00303 | 0.163 |  | 77.4 | 0.0348 | 0.797 | 0.0238 | 5 |
| quad-linear-h0.2 | 1519 | Elmer UMFPACK | 0.01 | 0 | 0.437 |  | 30.9 | 0.0355 | 0.82 | 5e-06 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript frontal | 0.229 | 0.171 | 0.361 | 0.123 | 81.2 | 0.0104 | 0.396 | 1.65e-12 | 5 |
| quad-linear-h0.1 | 5725 | FEAScript sparse LU | 0.26 | 0.203 | 0.392 | 0.289 | 94.3 | 0.0104 | 0.396 | 0 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem SuperLU | 0.0364 | 0.0137 | 0.228 |  | 79.8 | 0.0104 | 0.396 | 2.05e-12 | 5 |
| quad-linear-h0.1 | 5725 | scikit-fem fine integration | 0.0513 | 0.0134 | 0.244 |  | 113 | 0.0102 | 0.383 | 0.0128 | 5 |
| quad-linear-h0.1 | 5725 | Elmer UMFPACK | 0.02 | 0.01 | 0.494 |  | 36.8 | 0.0104 | 0.396 | 5e-06 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript frontal | 0.836 | 0.695 | 1.01 | 0.709 | 151 | 0.00296 | 0.191 | 1.35e-11 | 5 |
| quad-linear-h0.05 | 22423 | FEAScript sparse LU | 0.741 | 0.609 | 0.909 | 0.949 | 153 | 0.00296 | 0.191 | 0 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem SuperLU | 0.163 | 0.0758 | 0.372 |  | 134 | 0.00296 | 0.191 | 6.03e-12 | 5 |
| quad-linear-h0.05 | 22423 | scikit-fem fine integration | 0.24 | 0.0734 | 0.448 |  | 260 | 0.00291 | 0.184 | 0.00666 | 5 |
| quad-linear-h0.05 | 22423 | Elmer UMFPACK | 0.07 | 0.04 | 0.557 |  | 66.1 | 0.00296 | 0.191 | 5e-06 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript frontal | 0.144 | 0.128 | 0.264 | 0.0498 | 71.2 | 0.0142 | 0.364 | 1.05e-12 | 5 |
| quad-quadratic-h0.4 | 1597 | FEAScript sparse LU | 0.128 | 0.104 | 0.251 | 0.118 | 72.5 | 0.0142 | 0.364 | 0 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem SuperLU | 0.00853 | 0.00291 | 0.198 |  | 68.3 | 0.0142 | 0.364 | 2.65e-11 | 5 |
| quad-quadratic-h0.4 | 1597 | scikit-fem fine integration | 0.0116 | 0.00281 | 0.199 |  | 71.4 | 0.014 | 0.358 | 0.00615 | 5 |
| quad-quadratic-h0.4 | 1597 | Elmer UMFPACK | 0 | 0 | 0.479 |  | 31.1 | 0.0142 | 0.364 | 5e-06 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript frontal | 0.232 | 0.197 | 0.359 | 0.0968 | 73.4 | 0.00365 | 0.177 | 3.47e-12 | 5 |
| quad-quadratic-h0.2 | 5953 | FEAScript sparse LU | 0.234 | 0.197 | 0.367 | 0.275 | 107 | 0.00365 | 0.177 | 0 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem SuperLU | 0.028 | 0.0148 | 0.219 |  | 81.1 | 0.00365 | 0.177 | 1.3e-11 | 5 |
| quad-quadratic-h0.2 | 5953 | scikit-fem fine integration | 0.0347 | 0.0143 | 0.227 |  | 93.3 | 0.00361 | 0.174 | 0.00318 | 5 |
| quad-quadratic-h0.2 | 5953 | Elmer UMFPACK | 0.01 | 0.01 | 0.499 |  | 38.6 | 0.00365 | 0.177 | 5e-06 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript frontal | 0.736 | 0.668 | 0.879 | 0.586 | 129 | 0.000934 | 0.0872 | 1.43e-11 | 5 |
| quad-quadratic-h0.1 | 22657 | FEAScript sparse LU | 0.789 | 0.712 | 0.944 | 1.09 | 208 | 0.000934 | 0.0872 | 0 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem SuperLU | 0.13 | 0.091 | 0.336 |  | 143 | 0.000934 | 0.0872 | 7.62e-12 | 5 |
| quad-quadratic-h0.1 | 22657 | scikit-fem fine integration | 0.16 | 0.0888 | 0.368 |  | 188 | 0.000923 | 0.0856 | 0.00162 | 5 |
| quad-quadratic-h0.1 | 22657 | Elmer UMFPACK | 0.06 | 0.04 | 0.596 |  | 67.2 | 0.000934 | 0.0872 | 5e-06 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript frontal | 6.97 | 6.8 | 7.19 | 6.59 | 472 | 0.000235 | 0.0432 | 1.44e-10 | 5 |
| quad-quadratic-h0.05 | 89209 | FEAScript sparse LU | 3.09 | 2.89 | 3.3 | 5.22 | 578 | 0.000235 | 0.0432 | 0 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem SuperLU | 0.8 | 0.654 | 1.06 |  | 449 | 0.000235 | 0.0432 | 3.54e-11 | 5 |
| quad-quadratic-h0.05 | 89209 | scikit-fem fine integration | 0.973 | 0.65 | 1.23 |  | 626 | 0.000232 | 0.0424 | 0.000816 | 5 |
| quad-quadratic-h0.05 | 89209 | Elmer UMFPACK | 0.32 | 0.23 | 1.13 |  | 177 | 0.000235 | 0.0432 | 5e-06 | 5 |
