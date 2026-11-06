set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'psi_min.png'
set title 'Primary vortex strength ψ_{min} (FEAScript 0.4.0, Intel(R) N100)' font 'Arial,15'
set logscale x 2; set xlabel 'Elements per side n (n × n mesh)'; set ylabel 'ψ_{min}'
set key top right
plot 'psi_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 pt 7 ps 1.0 lc rgb '#2a78d6' t 'FEAScript', \
     'psi_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 pt 9 ps 1.6 lc rgb '#1baf7a' t 'Elmer', \
     'psi_scikit_fem_SuperLU.dat' u 1:2 w lp lw 2 pt 4 ps 1.6 lc rgb '#c0392b' t 'scikit-fem'
