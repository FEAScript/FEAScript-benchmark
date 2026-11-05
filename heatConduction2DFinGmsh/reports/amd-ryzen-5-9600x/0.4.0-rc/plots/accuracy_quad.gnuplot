set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
set output 'accuracy_quad.png'
set title 'RMS nodal error vs exact solution, quadrilaterals (FEAScript 0.4.0-rc, AMD Ryzen 5 9600X 6-Core Processor)' font 'Arial,14'
set xlabel 'Number of nodes'
set ylabel 'RMS error (K)'
set key bottom left
plot 'err_quad_linear_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 dt 1 pt 7 ps 1.0 lc rgb '#2a78d6' t 'FEAScript (linear)', \
     'err_quad_linear_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 dt 1 pt 9 ps 1.6 lc rgb '#1baf7a' t 'Elmer (linear)', \
     'err_quad_linear_scikit_fem_SuperLU.dat' u 1:2 w lp lw 2 dt 1 pt 4 ps 1.6 lc rgb '#c0392b' t 'scikit-fem (linear)', \
     'err_quad_linear_scikit_fem_fine_integration.dat' u 1:2 w lp lw 2 dt 1 pt 15 ps 1.6 lc rgb '#7b52c7' t 'scikit-fem fine integration (linear)', \
     'err_quad_quadratic_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 dt 2 pt 7 ps 1.0 lc rgb '#2a78d6' t 'FEAScript (quadratic)', \
     'err_quad_quadratic_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 dt 2 pt 9 ps 1.6 lc rgb '#1baf7a' t 'Elmer (quadratic)', \
     'err_quad_quadratic_scikit_fem_SuperLU.dat' u 1:2 w lp lw 2 dt 2 pt 4 ps 1.6 lc rgb '#c0392b' t 'scikit-fem (quadratic)', \
     'err_quad_quadratic_scikit_fem_fine_integration.dat' u 1:2 w lp lw 2 dt 2 pt 15 ps 1.6 lc rgb '#7b52c7' t 'scikit-fem fine integration (quadratic)'
