| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.052 | 0.0418 | 0.246 | 0.044 | 61.5 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.147 | 0.126 | 0.357 | 0.0466 | 65.4 | 0.113 | 1.02 | 3.13e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0453 | 0.0196 | 0.253 | 0.0284 | 57.7 | 0.113 | 1.02 | 3.35e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00933 | 0.0013 | 0.321 |  | 60 | 0.113 | 1.02 | 2.84e-13 | 2.27e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.3 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.5 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.03 |  | 32.6 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.239 | 0.21 | 0.468 | 0.0991 | 69.5 | 0.0316 | 0.574 | 7.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.298 | 0.231 | 0.496 | 0.162 | 66.9 | 0.0316 | 0.574 | 3.41e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.155 | 0.105 | 0.34 | 0.151 | 63.3 | 0.0316 | 0.574 | 9.66e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0142 | 0.00356 | 0.328 |  | 61.1 | 0.0316 | 0.574 | 1.17e-12 | 2.73e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 30.9 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.4 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 33.7 | 0.0316 | 0.574 | 9.66e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.314 | 0.258 | 0.503 | 0.195 | 71.4 | 0.00883 | 0.307 | 2.25e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.48 | 0.406 | 0.668 | 0.462 | 82.4 | 0.00883 | 0.307 | 9.15e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 1.21 | 1.14 | 1.4 | 1.29 | 65.1 | 0.00885 | 0.307 | 0.000273 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0371 | 0.0148 | 0.35 |  | 66.7 | 0.00883 | 0.307 | 1.85e-12 | 1.08e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 33.6 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.6 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 38.3 | 0.00883 | 0.307 | 2.53e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.921 | 0.818 | 1.11 | 0.689 | 98.2 | 0.00244 | 0.159 | 1.03e-11 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.29 | 1.15 | 1.52 | 1.2 | 140 | 0.00244 | 0.159 | 4.44e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.142 | 0.0759 | 0.456 |  | 93.9 | 0.00244 | 0.159 | 1.49e-11 | 4.45e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.11 | 2.22 |  | 41.4 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.09 | 0.05 | 2.16 |  | 51.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.17 |  | 55.6 | 0.00244 | 0.159 | 1.04e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 6.2 | 5.97 | 6.43 | 5.52 | 253 | 0.000666 | 0.0812 | 7.29e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 4.56 | 4.3 | 4.8 | 4.65 | 333 | 0.000666 | 0.0812 | 1.86e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.73 | 0.446 | 1.04 |  | 210 | 0.000666 | 0.0812 | 3.27e-11 | 1.69e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.03 | 0.85 | 3.2 |  | 75.5 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.48 | 0.3 | 2.66 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.48 | 0.3 | 2.66 |  | 133 | 0.000666 | 0.0812 | 3.04e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.313 | 0.259 | 0.498 | 0.209 | 72.1 | 0.00938 | 0.312 | 6.91e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.45 | 0.382 | 0.643 | 0.425 | 80.8 | 0.00938 | 0.312 | 7.82e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 1.07 | 1.01 | 1.26 | 1.03 | 64.7 | 0.0094 | 0.312 | 0.00026 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.035 | 0.0137 | 0.351 |  | 66.4 | 0.00938 | 0.312 | 3.69e-12 | 4.95e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 32.8 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.2 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.05 |  | 37.5 | 0.00938 | 0.312 | 1.62e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0491 | 0.0436 | 0.234 | 0.0495 | 59 | 0.0667 | 0.8 | 7.96e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.161 | 0.134 | 0.349 | 0.0581 | 64.9 | 0.0667 | 0.8 | 7.11e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0523 | 0.0301 | 0.237 | 0.038 | 58.1 | 0.0667 | 0.8 | 4.05e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.0118 | 0.00116 | 0.325 |  | 60.2 | 0.0667 | 0.8 | 7.39e-13 | 5.12e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.6 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.9 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.04 |  | 32.8 | 0.0667 | 0.8 | 4.26e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.267 | 0.246 | 0.457 | 0.0755 | 69.4 | 0.0169 | 0.394 | 3.21e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.272 | 0.224 | 0.461 | 0.146 | 66.5 | 0.0169 | 0.394 | 2.56e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.247 | 0.2 | 0.432 | 0.199 | 63.1 | 0.0169 | 0.394 | 0.000115 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0157 | 0.00312 | 0.328 |  | 61.1 | 0.0169 | 0.394 | 3.11e-12 | 8.53e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 31.4 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 32.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 34.1 | 0.0169 | 0.394 | 1.73e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.355 | 0.307 | 0.541 | 0.184 | 70.4 | 0.00426 | 0.196 | 1.07e-11 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.507 | 0.427 | 0.727 | 0.585 | 81 | 0.00426 | 0.196 | 9.32e-12 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0364 | 0.0159 | 0.355 |  | 67.1 | 0.00426 | 0.196 | 8.92e-12 | 1.48e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.08 |  | 33.3 | 0.00426 | 0.196 | 6.74e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 36 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 38.2 | 0.00426 | 0.196 | 6.28e-12 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.808 | 0.726 | 0.992 | 0.564 | 84.9 | 0.00107 | 0.0975 | 3.36e-11 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.36 | 1.24 | 1.56 | 1.26 | 148 | 0.00107 | 0.0975 | 3.75e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.17 | 0.111 | 0.489 |  | 97.3 | 0.00107 | 0.0975 | 3.94e-11 | 9.44e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.12 | 2.32 |  | 41 | 0.00107 | 0.0975 | 3.62e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.09 | 0.06 | 2.25 |  | 54.3 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.26 |  | 57.7 | 0.00107 | 0.0975 | 1.64e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 4.86 | 4.72 | 5.05 | 4.43 | 233 | 0.000268 | 0.0487 | 1.13e-10 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.52 | 5.28 | 5.74 | 5.55 | 343 | 0.000268 | 0.0487 | 1.1e-10 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.24 | 1.03 | 1.55 |  | 256 | 0.000268 | 0.0487 | 1.53e-10 | 7.09e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.21 | 1.07 | 3.71 |  | 72.5 | 0.000268 | 0.0487 | 9.83e-06 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.64 | 0.5 | 3.15 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.01 |  | 131 | 0.000268 | 0.0487 | 7.6e-11 |  | 5 |
