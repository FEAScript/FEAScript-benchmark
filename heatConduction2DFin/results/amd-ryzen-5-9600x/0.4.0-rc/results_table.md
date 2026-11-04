| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0186 | 0.0128 | 0.136 | 0.0153 | 61.3 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0496 | 0.0424 | 0.192 | 0.0246 | 66.2 | 0.113 | 1.02 | 4.96e-06 | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0156 | 0.0083 | 0.0991 | 0.0113 | 57.2 | 0.113 | 1.02 | 2.8e-05 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.47 |  | 29.8 | 0.113 | 1.02 | 1e-06 | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.471 |  | 30 | 0.113 | 1.02 | 0 | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.47 |  | 31.9 | 0.113 | 1.02 | 0 | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.0918 | 0.0787 | 0.219 | 0.0416 | 69.8 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.0997 | 0.0795 | 0.225 | 0.0713 | 67.3 | 0.0316 | 0.574 | 4.99e-06 | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0625 | 0.042 | 0.146 | 0.0426 | 63.1 | 0.0316 | 0.574 | 7.25e-05 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.426 |  | 30.4 | 0.0316 | 0.574 | 1e-05 | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.474 |  | 30.9 | 0.0316 | 0.574 | 0 | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 33.1 | 0.0316 | 0.574 | 0 | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.125 | 0.102 | 0.245 | 0.067 | 71.7 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.181 | 0.157 | 0.302 | 0.2 | 82.1 | 0.00883 | 0.307 | 5e-06 | 5 |
| linear-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.476 |  | 33 | 0.00883 | 0.307 | 1e-05 | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.482 |  | 35 | 0.00883 | 0.307 | 0 | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.485 |  | 37.5 | 0.00883 | 0.307 | 0 | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.367 | 0.323 | 0.493 | 0.255 | 96.8 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.514 | 0.468 | 0.621 | 0.674 | 140 | 0.00244 | 0.159 | 5e-06 | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.525 |  | 41 | 0.00244 | 0.159 | 1e-05 | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.51 |  | 51 | 0.00244 | 0.159 | 0 | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.523 |  | 54.8 | 0.00244 | 0.159 | 0 | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 2.38 | 2.3 | 2.51 | 2.23 | 255 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 1.99 | 1.89 | 2.13 | 4.12 | 346 | 0.000666 | 0.0812 | 5e-06 | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.878 |  | 75.1 | 0.000666 | 0.0812 | 3e-05 | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.715 |  | 121 | 0.000666 | 0.0812 | 0 | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.747 |  | 131 | 0.000666 | 0.0812 | 0 | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.126 | 0.103 | 0.246 | 0.0763 | 71.9 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.18 | 0.155 | 0.296 | 0.186 | 80.4 | 0.00938 | 0.312 | 5e-06 | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.411 | 0.387 | 0.529 | 0.349 | 64.8 | 0.00939 | 0.312 | 0.000189 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.477 |  | 32.3 | 0.00938 | 0.312 | 1e-05 | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.481 |  | 34.7 | 0.00938 | 0.312 | 0 | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.482 |  | 36.7 | 0.00938 | 0.312 | 0 | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0174 | 0.0156 | 0.0985 | 0.0182 | 58.5 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0568 | 0.0488 | 0.191 | 0.0187 | 65.6 | 0.0667 | 0.8 | 4.99e-06 | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.019 | 0.011 | 0.1 | 0.0159 | 57.6 | 0.0667 | 0.8 | 2.75e-05 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.468 |  | 29.9 | 0.0667 | 0.8 | 1e-05 | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.469 |  | 30.2 | 0.0667 | 0.8 | 0 | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.469 |  | 32.1 | 0.0667 | 0.8 | 0 | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.065 | 0.0559 | 0.211 | 0.0322 | 69.3 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.111 | 0.0921 | 0.227 | 0.0738 | 67.1 | 0.0169 | 0.394 | 4.99e-06 | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0955 | 0.0768 | 0.216 | 0.0761 | 63.3 | 0.0169 | 0.394 | 7.04e-05 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.474 |  | 30.8 | 0.0169 | 0.394 | 1e-06 | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.474 |  | 31.3 | 0.0169 | 0.394 | 0 | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.473 |  | 33.3 | 0.0169 | 0.394 | 0 | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.148 | 0.127 | 0.27 | 0.0662 | 70.2 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.185 | 0.162 | 0.307 | 0.205 | 81.6 | 0.00426 | 0.196 | 5e-06 | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.483 |  | 32.7 | 0.00426 | 0.196 | 1e-05 | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.492 |  | 35.2 | 0.00426 | 0.196 | 0 | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.492 |  | 37.4 | 0.00426 | 0.196 | 0 | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.329 | 0.294 | 0.452 | 0.215 | 84.6 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.525 | 0.487 | 0.648 | 0.689 | 137 | 0.00107 | 0.0975 | 5e-06 | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.556 |  | 40.3 | 0.00107 | 0.0975 | 1e-05 | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.536 |  | 53.5 | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.546 |  | 56.7 | 0.00107 | 0.0975 | 0 | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 1.94 | 1.88 | 2.06 | 1.82 | 235 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.3 | 2.21 | 2.44 | 4.11 | 344 | 0.000268 | 0.0487 | 5e-06 | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 1.02 |  | 71.9 | 0.000268 | 0.0487 | 2e-05 | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.25 | 0.2 | 0.877 |  | 141 | 0.000268 | 0.0487 | 0 | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.25 | 0.19 | 0.877 |  | 129 | 0.000268 | 0.0487 | 1e-06 | 5 |
