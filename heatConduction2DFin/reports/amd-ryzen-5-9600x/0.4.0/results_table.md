| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.022 | 0.0156 | 0.136 | 0.0145 | 61.2 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0521 | 0.0445 | 0.191 | 0.0188 | 65.2 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0156 | 0.00815 | 0.1 | 0.0108 | 57.8 | 0.113 | 1.02 | 3.71e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00344 | 0.000558 | 0.191 |  | 59.3 | 0.113 | 1.02 | 4.96e-06 | 2.27e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 28.8 | 0.113 | 1.02 | 1e-06 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.455 |  | 29.1 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.474 |  | 30.8 | 0.113 | 1.02 | 0 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.0941 | 0.0802 | 0.221 | 0.0462 | 69.3 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.104 | 0.0832 | 0.232 | 0.0627 | 66.8 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0625 | 0.0411 | 0.192 | 0.0435 | 63.2 | 0.0316 | 0.574 | 9.99e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00549 | 0.00156 | 0.192 |  | 60.4 | 0.0316 | 0.574 | 4.99e-06 | 2.7e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.465 |  | 29.3 | 0.0316 | 0.574 | 1e-05 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.473 |  | 29.9 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.476 |  | 31.9 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.128 | 0.105 | 0.242 | 0.0687 | 70.8 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.196 | 0.168 | 0.327 | 0.204 | 82.6 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 0.454 | 0.427 | 0.605 | 0.388 | 64.6 | 0.00885 | 0.307 | 0.000276 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0151 | 0.00642 | 0.198 |  | 66.1 | 0.00883 | 0.307 | 5e-06 | 1.08e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.487 |  | 32 | 0.00883 | 0.307 | 1e-05 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.472 |  | 34.2 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.479 |  | 36.5 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.368 | 0.324 | 0.498 | 0.261 | 96.4 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.512 | 0.463 | 0.64 | 0.674 | 140 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0519 | 0.0272 | 0.224 |  | 93.3 | 0.00244 | 0.159 | 5e-06 | 4.45e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.526 |  | 40 | 0.00244 | 0.159 | 1e-05 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.513 |  | 50.1 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.522 |  | 53.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 2.4 | 2.31 | 2.53 | 2.19 | 255 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 1.96 | 1.86 | 2.11 | 3.28 | 347 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.243 | 0.153 | 0.418 |  | 209 | 0.000666 | 0.0812 | 5e-06 | 1.69e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.884 |  | 73.9 | 0.000666 | 0.0812 | 3e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.14 | 0.724 |  | 121 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.17 | 0.75 |  | 130 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.127 | 0.103 | 0.251 | 0.0767 | 71.8 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.181 | 0.154 | 0.308 | 0.191 | 78.8 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.402 | 0.376 | 0.527 | 0.344 | 64.2 | 0.0094 | 0.312 | 0.000265 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0137 | 0.00565 | 0.191 |  | 65.7 | 0.00938 | 0.312 | 5e-06 | 5.06e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.485 |  | 31.4 | 0.00938 | 0.312 | 1e-05 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.484 |  | 33.7 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.484 |  | 35.7 | 0.00938 | 0.312 | 0 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0191 | 0.0174 | 0.105 | 0.0178 | 58.3 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0553 | 0.0471 | 0.192 | 0.0196 | 65.2 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.02 | 0.0116 | 0.138 | 0.0168 | 57.9 | 0.0667 | 0.8 | 4.44e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00404 | 0.000496 | 0.191 |  | 59.5 | 0.0667 | 0.8 | 4.99e-06 | 4.83e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.469 |  | 28.9 | 0.0667 | 0.8 | 1e-05 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.468 |  | 29.2 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 31 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.112 | 0.103 | 0.235 | 0.0324 | 69.5 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.108 | 0.0891 | 0.232 | 0.0696 | 67.2 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0934 | 0.0743 | 0.218 | 0.0753 | 63 | 0.0169 | 0.394 | 0.000118 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0055 | 0.00131 | 0.192 |  | 60.5 | 0.0169 | 0.394 | 4.99e-06 | 9.66e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.472 |  | 29.6 | 0.0169 | 0.394 | 1e-06 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.475 |  | 30.4 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.475 |  | 32.2 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.149 | 0.128 | 0.274 | 0.066 | 69.9 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.185 | 0.16 | 0.311 | 0.217 | 82 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0133 | 0.00633 | 0.192 |  | 66.3 | 0.00426 | 0.196 | 5e-06 | 1.59e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.494 |  | 31.6 | 0.00426 | 0.196 | 1e-05 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.491 |  | 34.3 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.491 |  | 36.3 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.328 | 0.293 | 0.453 | 0.215 | 84.8 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.532 | 0.491 | 0.623 | 0.713 | 141 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0601 | 0.0403 | 0.232 |  | 96.6 | 0.00107 | 0.0975 | 5e-06 | 9.15e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.557 |  | 39.2 | 0.00107 | 0.0975 | 1e-05 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.537 |  | 52.5 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.543 |  | 55.5 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 1.95 | 1.89 | 2.09 | 1.76 | 234 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.32 | 2.23 | 2.46 | 4.04 | 344 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.406 | 0.345 | 0.582 |  | 256 | 0.000268 | 0.0487 | 5e-06 | 7.18e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 1.02 |  | 70.7 | 0.000268 | 0.0487 | 2e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.26 | 0.21 | 0.901 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.25 | 0.19 | 0.884 |  | 128 | 0.000268 | 0.0487 | 1e-06 |  | 5 |
