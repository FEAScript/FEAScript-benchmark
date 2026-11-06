| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.052 | 0.0418 | 0.246 | 0.044 | 61.5 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.141 | 0.121 | 0.326 | 0.0556 | 65.1 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0453 | 0.0196 | 0.253 | 0.0284 | 57.7 | 0.113 | 1.02 | 3.71e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00933 | 0.0013 | 0.321 |  | 60 | 0.113 | 1.02 | 4.96e-06 | 2.27e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.3 | 0.113 | 1.02 | 1e-06 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.5 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.03 |  | 32.6 | 0.113 | 1.02 | 0 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.239 | 0.21 | 0.468 | 0.0991 | 69.5 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.247 | 0.195 | 0.437 | 0.157 | 66.9 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.155 | 0.105 | 0.34 | 0.151 | 63.3 | 0.0316 | 0.574 | 9.99e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0142 | 0.00356 | 0.328 |  | 61.1 | 0.0316 | 0.574 | 4.99e-06 | 2.73e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 30.9 | 0.0316 | 0.574 | 1e-05 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.4 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 33.7 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.314 | 0.258 | 0.503 | 0.195 | 71.4 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.457 | 0.388 | 0.648 | 0.462 | 81.7 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 1.21 | 1.14 | 1.4 | 1.29 | 65.1 | 0.00885 | 0.307 | 0.000276 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0371 | 0.0148 | 0.35 |  | 66.7 | 0.00883 | 0.307 | 5e-06 | 1.08e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 33.6 | 0.00883 | 0.307 | 1e-05 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.6 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 38.3 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.921 | 0.818 | 1.11 | 0.689 | 98.2 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.23 | 1.1 | 1.42 | 1.58 | 139 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.142 | 0.0759 | 0.456 |  | 93.9 | 0.00244 | 0.159 | 5e-06 | 4.45e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.11 | 2.22 |  | 41.4 | 0.00244 | 0.159 | 1e-05 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.09 | 0.05 | 2.16 |  | 51.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.17 |  | 55.6 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 6.2 | 5.97 | 6.43 | 5.52 | 253 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 4.68 | 4.43 | 4.89 | 8.09 | 347 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.73 | 0.446 | 1.04 |  | 210 | 0.000666 | 0.0812 | 5e-06 | 1.69e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.03 | 0.85 | 3.2 |  | 75.5 | 0.000666 | 0.0812 | 3e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.48 | 0.3 | 2.66 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.48 | 0.3 | 2.66 |  | 133 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.313 | 0.259 | 0.498 | 0.209 | 72.1 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.441 | 0.375 | 0.623 | 0.446 | 80.8 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 1.07 | 1.01 | 1.26 | 1.03 | 64.7 | 0.0094 | 0.312 | 0.000265 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.035 | 0.0137 | 0.351 |  | 66.4 | 0.00938 | 0.312 | 5e-06 | 4.95e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.07 |  | 32.8 | 0.00938 | 0.312 | 1e-05 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 35.2 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.05 |  | 37.5 | 0.00938 | 0.312 | 0 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0491 | 0.0436 | 0.234 | 0.0495 | 59 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.147 | 0.124 | 0.331 | 0.0536 | 64.8 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0523 | 0.0301 | 0.237 | 0.038 | 58.1 | 0.0667 | 0.8 | 4.44e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.0118 | 0.00116 | 0.325 |  | 60.2 | 0.0667 | 0.8 | 4.99e-06 | 5.12e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.6 | 0.0667 | 0.8 | 1e-05 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.9 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.04 |  | 32.8 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.267 | 0.246 | 0.457 | 0.0755 | 69.4 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.257 | 0.21 | 0.443 | 0.158 | 67.2 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.247 | 0.2 | 0.432 | 0.199 | 63.1 | 0.0169 | 0.394 | 0.000118 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0157 | 0.00312 | 0.328 |  | 61.1 | 0.0169 | 0.394 | 4.99e-06 | 8.53e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 31.4 | 0.0169 | 0.394 | 1e-06 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 32.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 34.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.355 | 0.307 | 0.541 | 0.184 | 70.4 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.453 | 0.392 | 0.636 | 0.453 | 82.5 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0364 | 0.0159 | 0.355 |  | 67.1 | 0.00426 | 0.196 | 5e-06 | 1.48e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.08 |  | 33.3 | 0.00426 | 0.196 | 1e-05 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 36 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 38.2 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.808 | 0.726 | 0.992 | 0.564 | 84.9 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.33 | 1.23 | 1.54 | 1.78 | 136 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.17 | 0.111 | 0.489 |  | 97.3 | 0.00107 | 0.0975 | 5e-06 | 9.44e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.12 | 2.32 |  | 41 | 0.00107 | 0.0975 | 1e-05 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.09 | 0.06 | 2.25 |  | 54.3 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.26 |  | 57.7 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 4.86 | 4.72 | 5.05 | 4.43 | 233 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.56 | 5.33 | 5.75 | 10.1 | 344 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.24 | 1.03 | 1.55 |  | 256 | 0.000268 | 0.0487 | 5e-06 | 7.09e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.21 | 1.07 | 3.71 |  | 72.5 | 0.000268 | 0.0487 | 1e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.64 | 0.5 | 3.15 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.01 |  | 131 | 0.000268 | 0.0487 | 1e-06 |  | 5 |
