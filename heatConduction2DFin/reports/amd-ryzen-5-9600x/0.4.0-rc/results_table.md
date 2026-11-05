| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0219 | 0.0161 | 0.118 | 0.0111 | 60.5 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0553 | 0.0478 | 0.19 | 0.0218 | 65.5 | 0.113 | 1.02 | 4.96e-06 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0157 | 0.00831 | 0.105 | 0.0108 | 56.6 | 0.113 | 1.02 | 2.8e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00336 | 0.000552 | 0.19 |  | 62.2 | 0.113 | 1.02 | 4.96e-06 | 3.41e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.456 |  | 28.6 | 0.113 | 1.02 | 1e-06 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.473 |  | 28.8 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 30.6 | 0.113 | 1.02 | 0 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.0912 | 0.0782 | 0.217 | 0.0415 | 69 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.0997 | 0.0795 | 0.221 | 0.0651 | 66.1 | 0.0316 | 0.574 | 4.99e-06 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0623 | 0.042 | 0.192 | 0.0419 | 62.3 | 0.0316 | 0.574 | 7.25e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00535 | 0.00154 | 0.191 |  | 63.3 | 0.0316 | 0.574 | 4.99e-06 | 3.27e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.473 |  | 29.2 | 0.0316 | 0.574 | 1e-05 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.471 |  | 29.7 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.473 |  | 31.6 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.125 | 0.102 | 0.25 | 0.0661 | 71 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.188 | 0.164 | 0.304 | 0.213 | 83.1 | 0.00883 | 0.307 | 5e-06 |  | 5 |
| linear-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0144 | 0.00603 | 0.191 |  | 68.8 | 0.00883 | 0.307 | 5e-06 | 1.01e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.484 |  | 31.8 | 0.00883 | 0.307 | 1e-05 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 33.9 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.486 |  | 36.2 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.365 | 0.321 | 0.488 | 0.259 | 97.3 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.514 | 0.467 | 0.635 | 0.679 | 143 | 0.00244 | 0.159 | 5e-06 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0519 | 0.0273 | 0.222 |  | 96 | 0.00244 | 0.159 | 5e-06 | 4.36e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.525 |  | 39.8 | 0.00244 | 0.159 | 1e-05 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.511 |  | 49.8 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.526 |  | 53.5 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 2.39 | 2.31 | 2.52 | 2.21 | 251 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 2 | 1.9 | 2.14 | 3.4 | 346 | 0.000666 | 0.0812 | 5e-06 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.242 | 0.153 | 0.418 |  | 212 | 0.000666 | 0.0812 | 5e-06 | 1.78e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.883 |  | 73.7 | 0.000666 | 0.0812 | 3e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.14 | 0.725 |  | 120 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.745 |  | 129 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.128 | 0.104 | 0.247 | 0.0656 | 71.1 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.181 | 0.156 | 0.299 | 0.193 | 81.8 | 0.00938 | 0.312 | 5e-06 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.413 | 0.389 | 0.538 | 0.352 | 63.7 | 0.00939 | 0.312 | 0.000189 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0138 | 0.00568 | 0.19 |  | 68.4 | 0.00938 | 0.312 | 5e-06 | 3.84e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.471 |  | 31.2 | 0.00938 | 0.312 | 1e-05 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 33.4 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.478 |  | 35.4 | 0.00938 | 0.312 | 0 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0186 | 0.0168 | 0.107 | 0.0198 | 57.8 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0558 | 0.0474 | 0.19 | 0.0302 | 64.4 | 0.0667 | 0.8 | 4.99e-06 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0192 | 0.011 | 0.108 | 0.0159 | 56.9 | 0.0667 | 0.8 | 2.75e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00398 | 0.00048 | 0.19 |  | 62.4 | 0.0667 | 0.8 | 4.99e-06 | 5.4e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 28.7 | 0.0667 | 0.8 | 1e-05 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.466 |  | 29 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.469 |  | 30.8 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.105 | 0.0993 | 0.216 | 0.0324 | 68.6 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.111 | 0.0923 | 0.23 | 0.0724 | 66.6 | 0.0169 | 0.394 | 4.99e-06 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0977 | 0.0791 | 0.215 | 0.0768 | 62.5 | 0.0169 | 0.394 | 7.04e-05 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0055 | 0.0013 | 0.191 |  | 63.2 | 0.0169 | 0.394 | 4.99e-06 | 1.14e-12 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.473 |  | 29.4 | 0.0169 | 0.394 | 1e-06 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.474 |  | 30.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 32 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.147 | 0.126 | 0.268 | 0.0661 | 70 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.192 | 0.169 | 0.311 | 0.198 | 83.1 | 0.00426 | 0.196 | 5e-06 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0132 | 0.00632 | 0.188 |  | 69.1 | 0.00426 | 0.196 | 5e-06 | 2.7e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.49 |  | 31.5 | 0.00426 | 0.196 | 1e-05 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.492 |  | 34 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0.01 | 0.489 |  | 36.2 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.339 | 0.303 | 0.452 | 0.231 | 84.7 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.532 | 0.494 | 0.65 | 0.686 | 134 | 0.00107 | 0.0975 | 5e-06 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0595 | 0.0401 | 0.192 |  | 99.3 | 0.00107 | 0.0975 | 5e-06 | 6.79e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.558 |  | 39.1 | 0.00107 | 0.0975 | 1e-05 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.536 |  | 52.2 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.546 |  | 55.1 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 1.95 | 1.89 | 2.08 | 1.83 | 234 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.31 | 2.22 | 2.45 | 4.03 | 344 | 0.000268 | 0.0487 | 5e-06 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.403 | 0.342 | 0.576 |  | 258 | 0.000268 | 0.0487 | 5e-06 | 6.92e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 1.02 |  | 70.6 | 0.000268 | 0.0487 | 2e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.26 | 0.21 | 0.895 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.24 | 0.19 | 0.876 |  | 128 | 0.000268 | 0.0487 | 1e-06 |  | 5 |
