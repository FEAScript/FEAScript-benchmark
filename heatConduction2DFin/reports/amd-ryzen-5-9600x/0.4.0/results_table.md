| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.022 | 0.0156 | 0.136 | 0.0145 | 61.2 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0529 | 0.0454 | 0.192 | 0.0178 | 64.6 | 0.113 | 1.02 | 3.13e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0156 | 0.00815 | 0.1 | 0.0108 | 57.8 | 0.113 | 1.02 | 3.35e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00344 | 0.000558 | 0.191 |  | 59.3 | 0.113 | 1.02 | 2.56e-13 | 2.27e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 28.8 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.455 |  | 29.1 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.474 |  | 30.8 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.0941 | 0.0802 | 0.221 | 0.0462 | 69.3 | 0.0316 | 0.574 | 7.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.103 | 0.0826 | 0.232 | 0.0537 | 67.4 | 0.0316 | 0.574 | 3.41e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0625 | 0.0411 | 0.192 | 0.0435 | 63.2 | 0.0316 | 0.574 | 9.66e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00549 | 0.00156 | 0.192 |  | 60.4 | 0.0316 | 0.574 | 1.22e-12 | 2.7e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.465 |  | 29.3 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.473 |  | 29.9 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.476 |  | 31.9 | 0.0316 | 0.574 | 7.82e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.128 | 0.105 | 0.242 | 0.0687 | 70.8 | 0.00883 | 0.307 | 2.25e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.188 | 0.161 | 0.315 | 0.172 | 82.7 | 0.00883 | 0.307 | 9.15e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 0.454 | 0.427 | 0.605 | 0.388 | 64.6 | 0.00885 | 0.307 | 0.000273 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0151 | 0.00642 | 0.198 |  | 66.1 | 0.00883 | 0.307 | 1.88e-12 | 1.08e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.487 |  | 32 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.472 |  | 34.2 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.479 |  | 36.5 | 0.00883 | 0.307 | 2.39e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.368 | 0.324 | 0.498 | 0.261 | 96.4 | 0.00244 | 0.159 | 1.03e-11 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.509 | 0.46 | 0.633 | 0.478 | 142 | 0.00244 | 0.159 | 4.44e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0519 | 0.0272 | 0.224 |  | 93.3 | 0.00244 | 0.159 | 1.49e-11 | 4.45e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.526 |  | 40 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.513 |  | 50.1 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.522 |  | 53.6 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 2.4 | 2.31 | 2.53 | 2.19 | 255 | 0.000666 | 0.0812 | 7.29e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 1.84 | 1.74 | 1.99 | 1.81 | 348 | 0.000666 | 0.0812 | 1.86e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.243 | 0.153 | 0.418 |  | 209 | 0.000666 | 0.0812 | 3.29e-11 | 1.69e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.884 |  | 73.9 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.14 | 0.724 |  | 121 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.17 | 0.75 |  | 130 | 0.000666 | 0.0812 | 3.02e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.127 | 0.103 | 0.251 | 0.0767 | 71.8 | 0.00938 | 0.312 | 6.91e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.184 | 0.157 | 0.304 | 0.168 | 81.7 | 0.00938 | 0.312 | 7.82e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.402 | 0.376 | 0.527 | 0.344 | 64.2 | 0.0094 | 0.312 | 0.00026 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0137 | 0.00565 | 0.191 |  | 65.7 | 0.00938 | 0.312 | 3.5e-12 | 5.06e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.485 |  | 31.4 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.484 |  | 33.7 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.484 |  | 35.7 | 0.00938 | 0.312 | 1.55e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0191 | 0.0174 | 0.105 | 0.0178 | 58.3 | 0.0667 | 0.8 | 5.4e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0557 | 0.0475 | 0.191 | 0.0219 | 65.7 | 0.0667 | 0.8 | 4.83e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.02 | 0.0116 | 0.138 | 0.0168 | 57.9 | 0.0667 | 0.8 | 4.05e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00404 | 0.000496 | 0.191 |  | 59.5 | 0.0667 | 0.8 | 4.55e-13 | 4.83e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.469 |  | 28.9 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.468 |  | 29.2 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 31 | 0.0667 | 0.8 | 5.68e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.112 | 0.103 | 0.235 | 0.0324 | 69.5 | 0.0169 | 0.394 | 2.5e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.108 | 0.0883 | 0.231 | 0.0687 | 66.5 | 0.0169 | 0.394 | 1.73e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0934 | 0.0743 | 0.218 | 0.0753 | 63 | 0.0169 | 0.394 | 0.000115 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0055 | 0.00131 | 0.192 |  | 60.5 | 0.0169 | 0.394 | 2.42e-12 | 9.66e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.472 |  | 29.6 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.475 |  | 30.4 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.475 |  | 32.2 | 0.0169 | 0.394 | 1.11e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.149 | 0.128 | 0.274 | 0.066 | 69.9 | 0.00426 | 0.196 | 6.28e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.187 | 0.162 | 0.313 | 0.168 | 82.4 | 0.00426 | 0.196 | 5.1e-12 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0133 | 0.00633 | 0.192 |  | 66.3 | 0.00426 | 0.196 | 4.77e-12 | 1.59e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.494 |  | 31.6 | 0.00426 | 0.196 | 6.52e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.491 |  | 34.3 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.491 |  | 36.3 | 0.00426 | 0.196 | 6.48e-12 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.328 | 0.293 | 0.453 | 0.215 | 84.8 | 0.00107 | 0.0975 | 2.53e-11 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.525 | 0.482 | 0.654 | 0.489 | 132 | 0.00107 | 0.0975 | 2.89e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0601 | 0.0403 | 0.232 |  | 96.6 | 0.00107 | 0.0975 | 3.4e-11 | 9.15e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.557 |  | 39.2 | 0.00107 | 0.0975 | 2.64e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.537 |  | 52.5 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.543 |  | 55.5 | 0.00107 | 0.0975 | 1.31e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 1.95 | 1.89 | 2.09 | 1.76 | 234 | 0.000268 | 0.0487 | 9.96e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.18 | 2.09 | 2.32 | 2.12 | 344 | 0.000268 | 0.0487 | 9.98e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.406 | 0.345 | 0.582 |  | 256 | 0.000268 | 0.0487 | 1.57e-10 | 7.18e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 1.02 |  | 70.7 | 0.000268 | 0.0487 | 1.87e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.26 | 0.21 | 0.901 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.25 | 0.19 | 0.884 |  | 128 | 0.000268 | 0.0487 | 8.56e-11 |  | 5 |
