| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.286 | 0.281 | 0.506 | 0.292 | 125 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.178 | 0.154 | 0.399 | 0.0724 | 72.4 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0419 | 0.0245 | 0.252 | 0.0189 | 67.1 | 0.113 | 1.02 | 0.000538 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.00936 | 0.00131 | 0.326 |  | 59.2 | 0.113 | 1.02 | 2.84e-13 | 3.41e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.1 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.03 |  | 30.3 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.03 |  | 32.4 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.361 | 0.354 | 0.62 | 0.284 | 131 | 0.0316 | 0.574 | 6.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.251 | 0.212 | 0.474 | 0.14 | 78 | 0.0316 | 0.574 | 3.84e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.131 | 0.0915 | 0.344 | 0.0982 | 69.6 | 0.0318 | 0.574 | 0.00113 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0143 | 0.00356 | 0.328 |  | 60.2 | 0.0316 | 0.574 | 1.17e-12 | 3.3e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.04 |  | 30.6 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.3 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 33.5 | 0.0316 | 0.574 | 9.66e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.902 | 0.876 | 1.12 | 0.876 | 206 | 0.00883 | 0.307 | 3.84e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.449 | 0.398 | 0.669 | 0.511 | 91.9 | 0.00883 | 0.307 | 8.58e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 1.04 | 0.988 | 1.25 | 0.91 | 81.5 | 0.00911 | 0.307 | 0.0023 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0369 | 0.0147 | 0.352 |  | 65.9 | 0.00883 | 0.307 | 1.85e-12 | 1.01e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.07 |  | 33.3 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.07 |  | 35.3 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.06 |  | 38.1 | 0.00883 | 0.307 | 2.53e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 29.6 | 29.5 | 30 | 29.5 | 1.66e+03 | 0.00244 | 0.159 | 9.18e-12 |  | 1 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.24 | 1.14 | 1.46 | 1.69 | 150 | 0.00244 | 0.159 | 4.39e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.142 | 0.0747 | 0.456 |  | 93.1 | 0.00244 | 0.159 | 1.49e-11 | 4.36e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.11 | 2.22 |  | 41.2 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.09 | 0.05 | 2.17 |  | 51.3 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.19 |  | 55.3 | 0.00244 | 0.159 | 1.04e-11 |  | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 4.93 | 4.69 | 5.17 | 9.58 | 351 | 0.000666 | 0.0812 | 1.93e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.726 | 0.446 | 1.05 |  | 209 | 0.000666 | 0.0812 | 3.27e-11 | 1.78e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.04 | 0.86 | 3.23 |  | 75.1 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.48 | 0.3 | 2.67 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.48 | 0.3 | 2.67 |  | 133 | 0.000666 | 0.0812 | 3.04e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.816 | 0.792 | 1.04 | 0.764 | 195 | 0.00938 | 0.312 | 5.54e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.438 | 0.391 | 0.674 | 0.444 | 88.5 | 0.00938 | 0.312 | 6.14e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 0.921 | 0.872 | 1.13 | 0.826 | 78.1 | 0.00965 | 0.312 | 0.00223 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.0351 | 0.0138 | 0.351 |  | 65.4 | 0.00938 | 0.312 | 3.69e-12 | 3.5e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.02 | 0.01 | 2.06 |  | 32.4 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.06 |  | 34.8 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.07 |  | 37.2 | 0.00938 | 0.312 | 1.62e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.519 | 0.514 | 0.743 | 0.343 | 132 | 0.0667 | 0.8 | 7.67e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.157 | 0.137 | 0.379 | 0.0593 | 72.6 | 0.0667 | 0.8 | 5.97e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0513 | 0.0306 | 0.263 | 0.0337 | 68.7 | 0.0667 | 0.8 | 0.000825 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.0118 | 0.00116 | 0.325 |  | 59.2 | 0.0667 | 0.8 | 7.39e-13 | 5.97e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.04 |  | 30.3 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.04 |  | 30.6 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.04 |  | 32.6 | 0.0667 | 0.8 | 4.26e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 1.05 | 1.05 | 1.27 | 0.944 | 157 | 0.0169 | 0.394 | 2.32e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.259 | 0.22 | 0.485 | 0.153 | 81.6 | 0.0169 | 0.394 | 2.96e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.213 | 0.177 | 0.43 | 0.168 | 70.1 | 0.017 | 0.394 | 0.00171 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0158 | 0.00312 | 0.335 |  | 60.1 | 0.0169 | 0.394 | 3.11e-12 | 9.95e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.05 |  | 31.1 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0 | 0 | 2.07 |  | 31.8 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.05 |  | 33.6 | 0.0169 | 0.394 | 1.73e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 27.4 | 27.4 | 27.7 | 25.3 | 645 | 0.00426 | 0.196 | 1.3e-11 |  | 1 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.446 | 0.39 | 0.663 | 0.495 | 93.3 | 0.00426 | 0.196 | 1.11e-11 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.0359 | 0.0156 | 0.349 |  | 66.1 | 0.00426 | 0.196 | 8.92e-12 | 2.53e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.09 |  | 33 | 0.00426 | 0.196 | 6.74e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.08 |  | 35.7 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 37.8 | 0.00426 | 0.196 | 6.28e-12 |  | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.3 | 1.2 | 1.51 | 1.7 | 153 | 0.00107 | 0.0975 | 3.77e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.171 | 0.112 | 0.49 |  | 96.4 | 0.00107 | 0.0975 | 3.94e-11 | 7.08e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.16 | 0.12 | 2.31 |  | 40.7 | 0.00107 | 0.0975 | 3.62e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.1 | 0.06 | 2.25 |  | 53.9 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.27 |  | 57.4 | 0.00107 | 0.0975 | 1.64e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.77 | 5.43 | 6.02 | 10.4 | 421 | 0.000268 | 0.0487 | 1.08e-10 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.24 | 1.03 | 1.56 |  | 256 | 0.000268 | 0.0487 | 1.53e-10 | 6.83e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.21 | 1.07 | 3.78 |  | 72.2 | 0.000268 | 0.0487 | 9.83e-06 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.64 | 0.5 | 3.16 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.37 | 3.01 |  | 131 | 0.000268 | 0.0487 | 7.6e-11 |  | 5 |
