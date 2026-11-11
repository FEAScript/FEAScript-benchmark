| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.101 | 0.0989 | 0.238 | 0.111 | 125 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0516 | 0.0452 | 0.196 | 0.0163 | 72.7 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0169 | 0.0105 | 0.174 | 0.00789 | 66 | 0.113 | 1.02 | 0.000538 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00332 | 0.00055 | 0.19 |  | 59.3 | 0.113 | 1.02 | 2.56e-13 | 3.41e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.469 |  | 28.8 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.469 |  | 29 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 30.7 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.131 | 0.129 | 0.267 | 0.11 | 131 | 0.0316 | 0.574 | 6.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.105 | 0.0887 | 0.24 | 0.0577 | 78.2 | 0.0316 | 0.574 | 3.84e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0508 | 0.0353 | 0.19 | 0.0349 | 69.4 | 0.0318 | 0.574 | 0.00113 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00538 | 0.00154 | 0.19 |  | 60.3 | 0.0316 | 0.574 | 1.22e-12 | 3.27e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 29.3 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.473 |  | 29.8 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 31.9 | 0.0316 | 0.574 | 7.82e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.294 | 0.284 | 0.424 | 0.271 | 207 | 0.00883 | 0.307 | 3.84e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.184 | 0.165 | 0.311 | 0.214 | 90.6 | 0.00883 | 0.307 | 8.58e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 0.381 | 0.362 | 0.513 | 0.354 | 76.7 | 0.00911 | 0.307 | 0.0023 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0144 | 0.00603 | 0.19 |  | 66.1 | 0.00883 | 0.307 | 1.88e-12 | 1.01e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.48 |  | 31.9 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 34 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.483 |  | 36.3 | 0.00883 | 0.307 | 2.39e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 3.13 | 3.09 | 3.33 | 3.41 | 1.67e+03 | 0.00244 | 0.159 | 9.18e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.512 | 0.471 | 0.647 | 0.681 | 150 | 0.00244 | 0.159 | 4.39e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0515 | 0.027 | 0.223 |  | 93.3 | 0.00244 | 0.159 | 1.49e-11 | 4.36e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.528 |  | 39.8 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.517 |  | 50 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.526 |  | 53.6 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 2.04 | 1.92 | 2.19 | 3.49 | 368 | 0.000666 | 0.0812 | 1.93e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.24 | 0.152 | 0.415 |  | 209 | 0.000666 | 0.0812 | 3.29e-11 | 1.78e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.88 |  | 73.9 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.717 |  | 120 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.747 |  | 129 | 0.000666 | 0.0812 | 3.02e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.281 | 0.271 | 0.417 | 0.258 | 198 | 0.00938 | 0.312 | 5.54e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.169 | 0.151 | 0.302 | 0.182 | 89.6 | 0.00938 | 0.312 | 6.14e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.344 | 0.325 | 0.478 | 0.312 | 80.2 | 0.00965 | 0.312 | 0.00223 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0136 | 0.00561 | 0.191 |  | 65.6 | 0.00938 | 0.312 | 3.5e-12 | 3.84e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.442 |  | 31.3 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.444 |  | 33.6 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.483 |  | 35.6 | 0.00938 | 0.312 | 1.55e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.2 | 0.198 | 0.338 | 0.125 | 133 | 0.0667 | 0.8 | 5.4e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0581 | 0.0507 | 0.199 | 0.0192 | 73.6 | 0.0667 | 0.8 | 3.69e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0199 | 0.0125 | 0.176 | 0.0138 | 68.4 | 0.0667 | 0.8 | 0.000825 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00393 | 0.000486 | 0.132 |  | 59.4 | 0.0667 | 0.8 | 4.55e-13 | 5.4e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.47 |  | 28.8 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.47 |  | 29.1 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 30.8 | 0.0667 | 0.8 | 5.68e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.395 | 0.392 | 0.532 | 0.333 | 160 | 0.0169 | 0.394 | 1.51e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.102 | 0.087 | 0.236 | 0.0788 | 80.7 | 0.0169 | 0.394 | 1.68e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0789 | 0.0647 | 0.212 | 0.0656 | 70.8 | 0.017 | 0.394 | 0.00171 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.00554 | 0.00131 | 0.193 |  | 60.5 | 0.0169 | 0.394 | 2.42e-12 | 1.14e-12 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.469 |  | 29.6 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.476 |  | 30.2 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.473 |  | 32 | 0.0169 | 0.394 | 1.11e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 11.2 | 11.2 | 11.3 | 10.7 | 646 | 0.00426 | 0.196 | 1e-11 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.181 | 0.158 | 0.314 | 0.212 | 92.5 | 0.00426 | 0.196 | 6.57e-12 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0132 | 0.0063 | 0.19 |  | 66.3 | 0.00426 | 0.196 | 4.77e-12 | 2.7e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.489 |  | 31.5 | 0.00426 | 0.196 | 6.52e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.49 |  | 34.2 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.491 |  | 36.1 | 0.00426 | 0.196 | 6.48e-12 |  | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.54 | 0.498 | 0.639 | 0.711 | 153 | 0.00107 | 0.0975 | 3.08e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0593 | 0.0397 | 0.23 |  | 96.6 | 0.00107 | 0.0975 | 3.4e-11 | 6.79e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.558 |  | 39.2 | 0.00107 | 0.0975 | 2.64e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.536 |  | 52.4 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.545 |  | 55.2 | 0.00107 | 0.0975 | 1.31e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.44 | 2.3 | 2.58 | 4.16 | 437 | 0.000268 | 0.0487 | 9.71e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.401 | 0.341 | 0.574 |  | 256 | 0.000268 | 0.0487 | 1.57e-10 | 6.92e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 1.02 |  | 70.7 | 0.000268 | 0.0487 | 1.87e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.25 | 0.2 | 0.883 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.24 | 0.19 | 0.876 |  | 128 | 0.000268 | 0.0487 | 8.56e-11 |  | 5 |
