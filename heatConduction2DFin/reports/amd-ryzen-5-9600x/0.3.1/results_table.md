| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.102 | 0.1 | 0.225 | 0.111 | 124 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0547 | 0.0479 | 0.197 | 0.0198 | 72.2 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0168 | 0.0105 | 0.171 | 0.00799 | 65.1 | 0.113 | 1.02 | 0.000538 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00339 | 0.000556 | 0.191 |  | 59.3 | 0.113 | 1.02 | 2.56e-13 | 3.41e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.42 |  | 28.7 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.452 |  | 29 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.452 |  | 30.7 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.133 | 0.131 | 0.267 | 0.112 | 130 | 0.0316 | 0.574 | 6.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.103 | 0.0875 | 0.236 | 0.0589 | 77.2 | 0.0316 | 0.574 | 3.84e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0511 | 0.0353 | 0.171 | 0.035 | 68.6 | 0.0318 | 0.574 | 0.00113 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00551 | 0.00158 | 0.191 |  | 60.2 | 0.0316 | 0.574 | 1.22e-12 | 3.27e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.448 |  | 29.3 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.458 |  | 29.8 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.467 |  | 31.7 | 0.0316 | 0.574 | 7.82e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.338 | 0.323 | 0.489 | 0.434 | 207 | 0.00883 | 0.307 | 3.84e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.187 | 0.165 | 0.331 | 0.231 | 90.6 | 0.00883 | 0.307 | 8.58e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 0.386 | 0.365 | 0.521 | 0.351 | 76.3 | 0.00911 | 0.307 | 0.0023 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0146 | 0.00609 | 0.192 |  | 66 | 0.00883 | 0.307 | 1.88e-12 | 1.01e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.467 |  | 31.9 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.438 |  | 34 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.442 |  | 36.3 | 0.00883 | 0.307 | 2.39e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 3.57 | 3.5 | 4.4 | 3.51 | 1.67e+03 | 0.00244 | 0.159 | 9.18e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.516 | 0.475 | 0.647 | 0.683 | 149 | 0.00244 | 0.159 | 4.39e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0516 | 0.027 | 0.183 |  | 93.1 | 0.00244 | 0.159 | 1.49e-11 | 4.36e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.525 |  | 39.8 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.504 |  | 49.9 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.483 |  | 53.5 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 2.05 | 1.93 | 2.25 | 3.58 | 367 | 0.000666 | 0.0812 | 1.93e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.24 | 0.152 | 0.376 |  | 209 | 0.000666 | 0.0812 | 3.29e-11 | 1.78e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.881 |  | 74 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.716 |  | 120 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.749 |  | 130 | 0.000666 | 0.0812 | 3.02e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.286 | 0.276 | 0.431 | 0.261 | 196 | 0.00938 | 0.312 | 5.54e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.287 | 0.257 | 0.383 | 0.211 | 88.8 | 0.00938 | 0.312 | 6.14e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.377 | 0.348 | 0.529 | 0.536 | 78.1 | 0.00965 | 0.312 | 0.00223 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0158 | 0.00671 | 0.194 |  | 65.6 | 0.00938 | 0.312 | 3.5e-12 | 3.84e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 0.52 |  | 31.2 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.449 |  | 33.7 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.482 |  | 35.6 | 0.00938 | 0.312 | 1.55e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.199 | 0.197 | 0.337 | 0.125 | 132 | 0.0667 | 0.8 | 5.4e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0595 | 0.0521 | 0.198 | 0.0271 | 72.4 | 0.0667 | 0.8 | 3.69e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0199 | 0.0126 | 0.193 | 0.0137 | 67.7 | 0.0667 | 0.8 | 0.000825 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00396 | 0.000481 | 0.192 |  | 59.4 | 0.0667 | 0.8 | 4.55e-13 | 5.4e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.423 |  | 28.8 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.432 |  | 29.1 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.432 |  | 31 | 0.0667 | 0.8 | 5.68e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.387 | 0.385 | 0.469 | 0.333 | 155 | 0.0169 | 0.394 | 1.51e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.105 | 0.0906 | 0.25 | 0.0691 | 79.8 | 0.0169 | 0.394 | 1.68e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.132 | 0.106 | 0.34 | 0.0676 | 70.3 | 0.017 | 0.394 | 0.00171 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.00941 | 0.00223 | 0.269 |  | 60.4 | 0.0169 | 0.394 | 2.42e-12 | 1.14e-12 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.461 |  | 29.6 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.432 |  | 30.4 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.459 |  | 32.1 | 0.0169 | 0.394 | 1.11e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 12.6 | 12.6 | 13.2 | 12.8 | 644 | 0.00426 | 0.196 | 1e-11 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.193 | 0.168 | 0.325 | 0.22 | 92.5 | 0.00426 | 0.196 | 6.57e-12 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0144 | 0.00675 | 0.244 |  | 66.3 | 0.00426 | 0.196 | 4.77e-12 | 2.7e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.505 |  | 31.5 | 0.00426 | 0.196 | 6.52e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.445 |  | 34.2 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.479 |  | 36.3 | 0.00426 | 0.196 | 6.48e-12 |  | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.568 | 0.526 | 0.724 | 0.733 | 152 | 0.00107 | 0.0975 | 3.08e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0615 | 0.0413 | 0.245 |  | 96.6 | 0.00107 | 0.0975 | 3.4e-11 | 6.79e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.579 |  | 39.3 | 0.00107 | 0.0975 | 2.64e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.554 |  | 52.5 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.565 |  | 55.4 | 0.00107 | 0.0975 | 1.31e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.58 | 2.42 | 2.77 | 4.41 | 436 | 0.000268 | 0.0487 | 9.71e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.431 | 0.356 | 0.612 |  | 256 | 0.000268 | 0.0487 | 1.57e-10 | 6.92e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.41 | 0.36 | 1.07 |  | 70.7 | 0.000268 | 0.0487 | 1.87e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.27 | 0.22 | 0.928 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.28 | 0.22 | 0.928 |  | 128 | 0.000268 | 0.0487 | 8.56e-11 |  | 5 |
