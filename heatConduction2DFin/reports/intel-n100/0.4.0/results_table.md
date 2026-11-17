| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0589 | 0.0454 | 0.285 | 0.0355 | 61.4 | 0.113 | 1.02 | 1.99e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.189 | 0.163 | 0.463 | 0.0607 | 64.8 | 0.113 | 1.02 | 4.26e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0713 | 0.0282 | 0.394 | 0.0364 | 58.4 | 0.113 | 1.02 | 3.35e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.011 | 0.00153 | 0.386 |  | 59.2 | 0.113 | 1.02 | 2.84e-13 | 3.69e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.08 |  | 29.8 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.05 |  | 30.1 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.07 |  | 32.3 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.248 | 0.207 | 0.473 | 0.156 | 69.4 | 0.0316 | 0.574 | 7.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.295 | 0.227 | 0.546 | 0.177 | 67 | 0.0316 | 0.574 | 3.35e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.165 | 0.107 | 0.367 | 0.108 | 63.3 | 0.0316 | 0.574 | 9.66e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0145 | 0.00369 | 0.421 |  | 60.2 | 0.0316 | 0.574 | 1.17e-12 | 2.53e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.09 |  | 30.6 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.06 |  | 31.1 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.08 |  | 33.3 | 0.0316 | 0.574 | 9.66e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.328 | 0.27 | 0.55 | 0.216 | 70.7 | 0.00883 | 0.307 | 1.65e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.535 | 0.446 | 0.728 | 0.458 | 80.7 | 0.00883 | 0.307 | 1.07e-11 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 1.25 | 1.17 | 1.46 | 1.13 | 64.4 | 0.00885 | 0.307 | 0.000273 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0436 | 0.0173 | 0.465 |  | 65.8 | 0.00883 | 0.307 | 1.85e-12 | 1.17e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.02 | 2.08 |  | 33.2 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.03 | 0.01 | 2.14 |  | 35.2 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.1 |  | 38 | 0.00883 | 0.307 | 2.53e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 1.14 | 1.04 | 1.42 | 0.722 | 94.9 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.53 | 1.36 | 1.81 | 1.33 | 129 | 0.00244 | 0.159 | 4.95e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.183 | 0.111 | 0.571 |  | 93.1 | 0.00244 | 0.159 | 1.49e-11 | 5.28e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.3 |  | 41.1 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.1 | 0.06 | 2.21 |  | 51.3 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.14 | 0.09 | 2.44 |  | 55.3 | 0.00244 | 0.159 | 1.04e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 6.22 | 5.99 | 6.36 | 6.43 | 248 | 0.000666 | 0.0812 | 8.03e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 4.73 | 4.35 | 5.07 | 4.54 | 329 | 0.000666 | 0.0812 | 1.96e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.84 | 0.523 | 1.22 |  | 209 | 0.000666 | 0.0812 | 3.27e-11 | 1.86e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.55 | 1.16 | 3.89 |  | 75.2 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.51 | 0.32 | 2.83 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.62 | 0.41 | 2.99 |  | 133 | 0.000666 | 0.0812 | 3.04e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.46 | 0.37 | 0.725 | 0.249 | 68.7 | 0.00938 | 0.312 | 6.76e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.682 | 0.558 | 0.917 | 0.467 | 81.2 | 0.00938 | 0.312 | 8.24e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 1.17 | 1.07 | 1.4 | 1.06 | 64.1 | 0.0094 | 0.312 | 0.00026 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0482 | 0.0179 | 0.569 |  | 65.4 | 0.00938 | 0.312 | 3.69e-12 | 5e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.11 |  | 32.4 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.03 | 0.01 | 2.13 |  | 34.9 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.09 |  | 37.2 | 0.00938 | 0.312 | 1.62e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0685 | 0.0593 | 0.303 | 0.0658 | 62.5 | 0.0667 | 0.8 | 9.09e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.216 | 0.18 | 0.451 | 0.069 | 65.6 | 0.0667 | 0.8 | 9.24e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0824 | 0.0426 | 0.345 | 0.0528 | 62.3 | 0.0667 | 0.8 | 4.05e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.0149 | 0.00167 | 0.438 |  | 59.4 | 0.0667 | 0.8 | 7.39e-13 | 3.98e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.06 |  | 30.4 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.09 |  | 30.7 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.08 |  | 32.5 | 0.0667 | 0.8 | 4.26e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.463 | 0.439 | 0.757 | 0.145 | 69.4 | 0.0169 | 0.394 | 3.45e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.353 | 0.289 | 0.586 | 0.214 | 67.3 | 0.0169 | 0.394 | 2.63e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.279 | 0.225 | 0.501 | 0.214 | 62.8 | 0.0169 | 0.394 | 0.000115 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0187 | 0.00362 | 0.393 |  | 60.1 | 0.0169 | 0.394 | 3.11e-12 | 9.09e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.06 |  | 31.1 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.07 |  | 31.8 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.08 |  | 33.8 | 0.0169 | 0.394 | 1.73e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.374 | 0.321 | 0.576 | 0.202 | 72.1 | 0.00426 | 0.196 | 1.17e-11 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.482 | 0.41 | 0.691 | 0.438 | 81.6 | 0.00426 | 0.196 | 1.24e-11 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.036 | 0.0157 | 0.355 |  | 66.1 | 0.00426 | 0.196 | 8.92e-12 | 3.95e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.02 | 2.09 |  | 33 | 0.00426 | 0.196 | 6.74e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.11 |  | 35.7 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 37.9 | 0.00426 | 0.196 | 6.28e-12 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.836 | 0.751 | 1.05 | 0.546 | 86.8 | 0.00107 | 0.0975 | 3.58e-11 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.4 | 1.27 | 1.61 | 1.33 | 132 | 0.00107 | 0.0975 | 3.78e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.175 | 0.114 | 0.502 |  | 96.4 | 0.00107 | 0.0975 | 3.94e-11 | 1.09e-11 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.32 |  | 40.8 | 0.00107 | 0.0975 | 3.62e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.1 | 0.06 | 2.27 |  | 54 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.29 |  | 57.5 | 0.00107 | 0.0975 | 1.64e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 5.31 | 5.13 | 5.84 | 4.76 | 233 | 0.000268 | 0.0487 | 1.09e-10 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.72 | 5.38 | 5.96 | 5.6 | 344 | 0.000268 | 0.0487 | 9.29e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.32 | 1.08 | 1.67 |  | 255 | 0.000268 | 0.0487 | 1.53e-10 | 7.71e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.26 | 1.13 | 3.84 |  | 72.2 | 0.000268 | 0.0487 | 9.83e-06 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.67 | 0.53 | 3.2 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.56 | 0.42 | 3.19 |  | 131 | 0.000268 | 0.0487 | 7.6e-11 |  | 5 |
