| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.0219 | 0.0151 | 0.109 | 0.0165 | 60.9 | 0.113 | 1.02 | 1.99e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.0555 | 0.0471 | 0.146 | 0.012 | 65.2 | 0.113 | 1.02 | 4.26e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0163 | 0.00812 | 0.107 | 0.0113 | 56.8 | 0.113 | 1.02 | 3.35e-05 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00367 | 0.000608 | 0.157 |  | 59.4 | 0.113 | 1.02 | 2.56e-13 | 3.69e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.424 |  | 28.5 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 0.431 |  | 28.9 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 30.7 | 0.113 | 1.02 | 2.27e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.0928 | 0.0789 | 0.22 | 0.0428 | 68.9 | 0.0316 | 0.574 | 7.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.105 | 0.0829 | 0.239 | 0.065 | 66.4 | 0.0316 | 0.574 | 3.35e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.0637 | 0.0416 | 0.198 | 0.0415 | 62.9 | 0.0316 | 0.574 | 9.66e-05 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.00542 | 0.00155 | 0.191 |  | 60.3 | 0.0316 | 0.574 | 1.22e-12 | 2.5e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.467 |  | 29.1 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0 | 0 | 0.472 |  | 29.8 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 31.6 | 0.0316 | 0.574 | 7.82e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.124 | 0.0998 | 0.252 | 0.0618 | 70.5 | 0.00883 | 0.307 | 1.65e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.19 | 0.16 | 0.318 | 0.184 | 80.1 | 0.00883 | 0.307 | 1.07e-11 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 0.453 | 0.424 | 0.578 | 0.396 | 63.8 | 0.00885 | 0.307 | 0.000273 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0146 | 0.00613 | 0.151 |  | 66.1 | 0.00883 | 0.307 | 1.88e-12 | 1.17e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.449 |  | 31.8 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.01 | 0 | 0.429 |  | 33.9 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.445 |  | 36.2 | 0.00883 | 0.307 | 2.39e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 0.36 | 0.318 | 0.509 | 0.228 | 94.7 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-160x80 | 13041 | FEAScript sparse LU | 0.509 | 0.456 | 0.643 | 0.489 | 129 | 0.00244 | 0.159 | 4.95e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.0522 | 0.0273 | 0.227 |  | 93.3 | 0.00244 | 0.159 | 1.49e-11 | 5.28e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.04 | 0.527 |  | 39.8 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.04 | 0.02 | 0.511 |  | 49.8 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.05 | 0.03 | 0.48 |  | 53.5 | 0.00244 | 0.159 | 1.08e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript frontal | 2.39 | 2.3 | 2.53 | 2.19 | 249 | 0.000666 | 0.0812 | 8.03e-11 |  | 5 |
| linear-320x160 | 51681 | FEAScript sparse LU | 1.83 | 1.72 | 1.98 | 1.82 | 330 | 0.000666 | 0.0812 | 1.96e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.24 | 0.151 | 0.414 |  | 209 | 0.000666 | 0.0812 | 3.29e-11 | 1.86e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 0.37 | 0.3 | 0.881 |  | 73.8 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.21 | 0.13 | 0.717 |  | 120 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.24 | 0.16 | 0.747 |  | 129 | 0.000666 | 0.0812 | 3.02e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.138 | 0.113 | 0.264 | 0.059 | 69.1 | 0.00938 | 0.312 | 6.76e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.183 | 0.154 | 0.308 | 0.177 | 79.6 | 0.00938 | 0.312 | 8.24e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.406 | 0.377 | 0.53 | 0.344 | 64.3 | 0.0094 | 0.312 | 0.00026 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0137 | 0.00563 | 0.187 |  | 65.6 | 0.00938 | 0.312 | 3.5e-12 | 5.12e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.486 |  | 31.1 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.01 | 0 | 0.483 |  | 33.5 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.01 | 0 | 0.484 |  | 35.5 | 0.00938 | 0.312 | 1.55e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.0199 | 0.0177 | 0.149 | 0.0151 | 62.2 | 0.0667 | 0.8 | 6.25e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.0552 | 0.0437 | 0.187 | 0.0304 | 65 | 0.0667 | 0.8 | 6.82e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0221 | 0.0116 | 0.187 | 0.0146 | 60.4 | 0.0667 | 0.8 | 4.05e-05 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.00401 | 0.000483 | 0.187 |  | 59.5 | 0.0667 | 0.8 | 4.55e-13 | 3.98e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.471 |  | 28.7 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 0.472 |  | 29.1 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 0.471 |  | 30.8 | 0.0667 | 0.8 | 5.68e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 0.114 | 0.104 | 0.22 | 0.0328 | 68.9 | 0.0169 | 0.394 | 2.7e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.119 | 0.0982 | 0.246 | 0.0667 | 67.1 | 0.0169 | 0.394 | 1.85e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.0941 | 0.0733 | 0.225 | 0.0749 | 62.6 | 0.0169 | 0.394 | 0.000115 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.00555 | 0.00134 | 0.187 |  | 60.3 | 0.0169 | 0.394 | 2.42e-12 | 9.95e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 0.463 |  | 29.5 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 0.487 |  | 30.2 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0 | 0 | 0.474 |  | 32 | 0.0169 | 0.394 | 1.11e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 0.151 | 0.128 | 0.273 | 0.0825 | 71.6 | 0.00426 | 0.196 | 7.7e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.195 | 0.167 | 0.314 | 0.188 | 80.9 | 0.00426 | 0.196 | 8.1e-12 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0132 | 0.00631 | 0.188 |  | 66.4 | 0.00426 | 0.196 | 4.77e-12 | 4.01e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.01 | 0.01 | 0.485 |  | 31.5 | 0.00426 | 0.196 | 6.52e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.01 | 0.01 | 0.487 |  | 34.1 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.01 | 0 | 0.473 |  | 36.2 | 0.00426 | 0.196 | 6.48e-12 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript frontal | 0.349 | 0.311 | 0.477 | 0.239 | 84.9 | 0.00107 | 0.0975 | 2.76e-11 |  | 5 |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 0.566 | 0.515 | 0.696 | 0.545 | 133 | 0.00107 | 0.0975 | 2.87e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.0608 | 0.0409 | 0.235 |  | 96.6 | 0.00107 | 0.0975 | 3.4e-11 | 1.04e-11 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.06 | 0.05 | 0.557 |  | 39.1 | 0.00107 | 0.0975 | 2.64e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.04 | 0.03 | 0.537 |  | 52.3 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.05 | 0.04 | 0.552 |  | 55.2 | 0.00107 | 0.0975 | 1.31e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript frontal | 1.95 | 1.88 | 2.08 | 1.78 | 233 | 0.000268 | 0.0487 | 9.56e-11 |  | 5 |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 2.24 | 2.13 | 2.38 | 2.17 | 344 | 0.000268 | 0.0487 | 8.17e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 0.408 | 0.346 | 0.544 |  | 256 | 0.000268 | 0.0487 | 1.57e-10 | 7.86e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 0.39 | 0.34 | 0.982 |  | 70.5 | 0.000268 | 0.0487 | 1.87e-05 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.26 | 0.21 | 0.871 |  | 140 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.25 | 0.19 | 0.842 |  | 128 | 0.000268 | 0.0487 | 8.56e-11 |  | 5 |
