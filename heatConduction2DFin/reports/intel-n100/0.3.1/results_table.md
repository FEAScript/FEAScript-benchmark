| case | nodes | code | solve | linsolve | process | warmWall | peakMemoryMB | rmsErr | maxErr | maxDiffVsElmerUMFPACK | maxDiffVsFEAScript | nruns |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| linear-20x10 | 231 | FEAScript frontal | 0.299 | 0.292 | 0.529 | 0.311 | 126 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript sparse LU | 0.146 | 0.128 | 0.374 | 0.0652 | 72 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-20x10 | 231 | FEAScript Jacobi | 0.0418 | 0.0241 | 0.257 | 0.0194 | 66.6 | 0.113 | 1.02 | 0.000538 |  | 5 |
| linear-20x10 | 231 | scikit-fem SuperLU | 0.0101 | 0.00139 | 0.345 |  | 62 | 0.113 | 1.02 | 2.84e-13 | 3.41e-13 | 5 |
| linear-20x10 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.04 |  | 30 | 0.113 | 1.02 | 5.44e-08 |  | 5 |
| linear-20x10 | 231 | Elmer UMFPACK | 0 | 0 | 2.06 |  | 30.3 | 0.113 | 1.02 | 0 |  | 5 |
| linear-20x10 | 231 | Elmer MUMPS | 0 | 0 | 2.04 |  | 32.4 | 0.113 | 1.02 | 2.84e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript frontal | 0.37 | 0.36 | 0.599 | 0.367 | 129 | 0.0316 | 0.574 | 6.11e-13 |  | 5 |
| linear-40x20 | 861 | FEAScript sparse LU | 0.268 | 0.228 | 0.522 | 0.132 | 78 | 0.0316 | 0.574 | 3.84e-12 |  | 5 |
| linear-40x20 | 861 | FEAScript Jacobi | 0.132 | 0.0931 | 0.348 | 0.0952 | 69.6 | 0.0318 | 0.574 | 0.00113 |  | 5 |
| linear-40x20 | 861 | scikit-fem SuperLU | 0.0143 | 0.00354 | 0.328 |  | 62.9 | 0.0316 | 0.574 | 1.17e-12 | 3.3e-12 | 5 |
| linear-40x20 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.05 |  | 30.6 | 0.0316 | 0.574 | 2.42e-07 |  | 5 |
| linear-40x20 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.04 |  | 31.2 | 0.0316 | 0.574 | 0 |  | 5 |
| linear-40x20 | 861 | Elmer MUMPS | 0.01 | 0 | 2.04 |  | 33.5 | 0.0316 | 0.574 | 9.66e-13 |  | 5 |
| linear-80x40 | 3321 | FEAScript frontal | 0.911 | 0.886 | 1.14 | 0.852 | 206 | 0.00883 | 0.307 | 3.84e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript sparse LU | 0.449 | 0.398 | 0.66 | 0.495 | 92.6 | 0.00883 | 0.307 | 8.58e-12 |  | 5 |
| linear-80x40 | 3321 | FEAScript Jacobi | 1.1 | 1.04 | 1.33 | 0.967 | 78.8 | 0.00911 | 0.307 | 0.0023 |  | 5 |
| linear-80x40 | 3321 | scikit-fem SuperLU | 0.0502 | 0.0175 | 0.422 |  | 68.5 | 0.00883 | 0.307 | 1.85e-12 | 1.01e-11 | 5 |
| linear-80x40 | 3321 | Elmer BiCGStab+ILU0 | 0.03 | 0.02 | 2.07 |  | 33.2 | 0.00883 | 0.307 | 6.48e-07 |  | 5 |
| linear-80x40 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 35.4 | 0.00883 | 0.307 | 0 |  | 5 |
| linear-80x40 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.07 |  | 37.9 | 0.00883 | 0.307 | 2.53e-12 |  | 5 |
| linear-160x80 | 13041 | FEAScript frontal | 33.2 | 33.1 | 33.6 | 27.9 | 1.67e+03 | 0.00244 | 0.159 | 9.18e-12 |  | 1 |
| linear-160x80 | 13041 | FEAScript sparse LU | 1.22 | 1.13 | 1.45 | 1.7 | 149 | 0.00244 | 0.159 | 4.39e-11 |  | 5 |
| linear-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-160x80 | 13041 | scikit-fem SuperLU | 0.156 | 0.081 | 0.528 |  | 93.5 | 0.00244 | 0.159 | 1.49e-11 | 4.36e-11 | 5 |
| linear-160x80 | 13041 | Elmer BiCGStab+ILU0 | 0.18 | 0.12 | 2.28 |  | 41.2 | 0.00244 | 0.159 | 6.32e-06 |  | 5 |
| linear-160x80 | 13041 | Elmer UMFPACK | 0.09 | 0.05 | 2.15 |  | 51.3 | 0.00244 | 0.159 | 0 |  | 5 |
| linear-160x80 | 13041 | Elmer MUMPS | 0.11 | 0.07 | 2.18 |  | 55.4 | 0.00244 | 0.159 | 1.04e-11 |  | 5 |
| linear-320x160 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | FEAScript sparse LU | 5.63 | 5.32 | 5.88 | 9.86 | 350 | 0.000666 | 0.0812 | 1.93e-10 |  | 5 |
| linear-320x160 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| linear-320x160 | 51681 | scikit-fem SuperLU | 0.757 | 0.464 | 1.09 |  | 210 | 0.000666 | 0.0812 | 3.27e-11 | 1.78e-10 | 5 |
| linear-320x160 | 51681 | Elmer BiCGStab+ILU0 | 1.05 | 0.86 | 3.22 |  | 75.2 | 0.000666 | 0.0812 | 2.1e-05 |  | 5 |
| linear-320x160 | 51681 | Elmer UMFPACK | 0.5 | 0.31 | 2.68 |  | 122 | 0.000666 | 0.0812 | 0 |  | 5 |
| linear-320x160 | 51681 | Elmer MUMPS | 0.49 | 0.31 | 2.68 |  | 133 | 0.000666 | 0.0812 | 3.04e-11 |  | 5 |
| linear-77x39 | 3120 | FEAScript frontal | 0.997 | 0.968 | 1.28 | 0.983 | 196 | 0.00938 | 0.312 | 5.54e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript sparse LU | 0.532 | 0.474 | 0.793 | 0.509 | 88.1 | 0.00938 | 0.312 | 6.14e-12 |  | 5 |
| linear-77x39 | 3120 | FEAScript Jacobi | 1.06 | 1 | 1.32 | 0.933 | 77 | 0.00965 | 0.312 | 0.00223 |  | 5 |
| linear-77x39 | 3120 | scikit-fem SuperLU | 0.044 | 0.0169 | 0.426 |  | 66.1 | 0.00938 | 0.312 | 3.69e-12 | 3.5e-12 | 5 |
| linear-77x39 | 3120 | Elmer BiCGStab+ILU0 | 0.03 | 0.01 | 2.09 |  | 32.7 | 0.00938 | 0.312 | 4.4e-07 |  | 5 |
| linear-77x39 | 3120 | Elmer UMFPACK | 0.02 | 0.01 | 2.1 |  | 35.1 | 0.00938 | 0.312 | 0 |  | 5 |
| linear-77x39 | 3120 | Elmer MUMPS | 0.02 | 0.01 | 2.07 |  | 37.5 | 0.00938 | 0.312 | 1.62e-12 |  | 5 |
| quadratic-10x5 | 231 | FEAScript frontal | 0.541 | 0.535 | 0.77 | 0.341 | 132 | 0.0667 | 0.8 | 7.67e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript sparse LU | 0.173 | 0.15 | 0.414 | 0.0895 | 72.5 | 0.0667 | 0.8 | 5.97e-13 |  | 5 |
| quadratic-10x5 | 231 | FEAScript Jacobi | 0.0515 | 0.031 | 0.26 | 0.0393 | 68.5 | 0.0667 | 0.8 | 0.000825 |  | 5 |
| quadratic-10x5 | 231 | scikit-fem SuperLU | 0.0135 | 0.0015 | 0.366 |  | 60.2 | 0.0667 | 0.8 | 7.39e-13 | 5.97e-13 | 5 |
| quadratic-10x5 | 231 | Elmer BiCGStab+ILU0 | 0 | 0 | 2.03 |  | 30.6 | 0.0667 | 0.8 | 1.29e-08 |  | 5 |
| quadratic-10x5 | 231 | Elmer UMFPACK | 0 | 0 | 2.08 |  | 30.9 | 0.0667 | 0.8 | 0 |  | 5 |
| quadratic-10x5 | 231 | Elmer MUMPS | 0 | 0 | 2.08 |  | 32.8 | 0.0667 | 0.8 | 4.26e-13 |  | 5 |
| quadratic-20x10 | 861 | FEAScript frontal | 1.43 | 1.42 | 1.99 | 1.18 | 157 | 0.0169 | 0.394 | 2.32e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript sparse LU | 0.378 | 0.325 | 0.78 | 0.218 | 81.5 | 0.0169 | 0.394 | 2.96e-12 |  | 5 |
| quadratic-20x10 | 861 | FEAScript Jacobi | 0.26 | 0.211 | 0.554 | 0.206 | 70.3 | 0.017 | 0.394 | 0.00171 |  | 5 |
| quadratic-20x10 | 861 | scikit-fem SuperLU | 0.0189 | 0.00366 | 0.418 |  | 60.9 | 0.0169 | 0.394 | 3.11e-12 | 9.95e-13 | 5 |
| quadratic-20x10 | 861 | Elmer BiCGStab+ILU0 | 0.01 | 0 | 2.11 |  | 31.4 | 0.0169 | 0.394 | 3.37e-08 |  | 5 |
| quadratic-20x10 | 861 | Elmer UMFPACK | 0.01 | 0 | 2.09 |  | 32.1 | 0.0169 | 0.394 | 0 |  | 5 |
| quadratic-20x10 | 861 | Elmer MUMPS | 0.01 | 0 | 2.12 |  | 34 | 0.0169 | 0.394 | 1.73e-12 |  | 5 |
| quadratic-40x20 | 3321 | FEAScript frontal | 30.7 | 30.7 | 31 | 25.2 | 647 | 0.00426 | 0.196 | 1.3e-11 |  | 1 |
| quadratic-40x20 | 3321 | FEAScript sparse LU | 0.46 | 0.403 | 0.676 | 0.498 | 93.6 | 0.00426 | 0.196 | 1.11e-11 |  | 5 |
| quadratic-40x20 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-40x20 | 3321 | scikit-fem SuperLU | 0.036 | 0.0157 | 0.355 |  | 67 | 0.00426 | 0.196 | 8.92e-12 | 2.53e-12 | 5 |
| quadratic-40x20 | 3321 | Elmer BiCGStab+ILU0 | 0.02 | 0.02 | 2.09 |  | 33.3 | 0.00426 | 0.196 | 6.74e-07 |  | 5 |
| quadratic-40x20 | 3321 | Elmer UMFPACK | 0.02 | 0.01 | 2.09 |  | 36 | 0.00426 | 0.196 | 0 |  | 5 |
| quadratic-40x20 | 3321 | Elmer MUMPS | 0.02 | 0.01 | 2.08 |  | 38.1 | 0.00426 | 0.196 | 6.28e-12 |  | 5 |
| quadratic-80x40 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | FEAScript sparse LU | 1.29 | 1.19 | 1.5 | 1.77 | 152 | 0.00107 | 0.0975 | 3.77e-11 |  | 5 |
| quadratic-80x40 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-80x40 | 13041 | scikit-fem SuperLU | 0.169 | 0.111 | 0.49 |  | 97.2 | 0.00107 | 0.0975 | 3.94e-11 | 7.08e-12 | 5 |
| quadratic-80x40 | 13041 | Elmer BiCGStab+ILU0 | 0.15 | 0.12 | 2.31 |  | 41 | 0.00107 | 0.0975 | 3.62e-06 |  | 5 |
| quadratic-80x40 | 13041 | Elmer UMFPACK | 0.09 | 0.06 | 2.24 |  | 54.2 | 0.00107 | 0.0975 | 0 |  | 5 |
| quadratic-80x40 | 13041 | Elmer MUMPS | 0.12 | 0.08 | 2.27 |  | 57.7 | 0.00107 | 0.0975 | 1.64e-11 |  | 5 |
| quadratic-160x80 |  | FEAScript frontal | out of memory |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | FEAScript sparse LU | 5.77 | 5.45 | 6 | 10.5 | 432 | 0.000268 | 0.0487 | 1.08e-10 |  | 5 |
| quadratic-160x80 |  | FEAScript Jacobi | not converged |  |  |  |  |  |  |  |  |  |
| quadratic-160x80 | 51681 | scikit-fem SuperLU | 1.23 | 1.03 | 1.55 |  | 256 | 0.000268 | 0.0487 | 1.53e-10 | 6.83e-11 | 5 |
| quadratic-160x80 | 51681 | Elmer BiCGStab+ILU0 | 1.18 | 1.05 | 3.69 |  | 72.6 | 0.000268 | 0.0487 | 9.83e-06 |  | 5 |
| quadratic-160x80 | 51681 | Elmer UMFPACK | 0.63 | 0.5 | 3.14 |  | 142 | 0.000268 | 0.0487 | 0 |  | 5 |
| quadratic-160x80 | 51681 | Elmer MUMPS | 0.5 | 0.36 | 3.01 |  | 131 | 0.000268 | 0.0487 | 7.6e-11 |  | 5 |
