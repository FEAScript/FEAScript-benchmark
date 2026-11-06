set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
set output 'solve_time_quad_quadratic.png'
set title 'Assembly + solve time, quadratic quadrilaterals (FEAScript 0.4.0, Intel(R) N100)' font 'Arial,14'
set xlabel 'Number of nodes'
set ylabel 'Time (s)'
set label 'Elmer timer resolution 0.01 s' at graph 0.98,0.05 right tc rgb '#777777'
plot 'solve_time_quad_quadratic_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 pt 7 ps 1.2 lc rgb '#2a78d6' t 'FEAScript sparse LU', \
     'solve_time_quad_quadratic_FEAScript_frontal.dat' u 1:2 w lp lw 2 pt 5 ps 1.2 lc rgb '#eb6834' t 'FEAScript frontal', \
     'solve_time_quad_quadratic_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 pt 9 ps 1.2 lc rgb '#1baf7a' t 'Elmer UMFPACK', \
     'solve_time_quad_quadratic_scikit_fem_SuperLU.dat' u 1:2 w lp lw 2 pt 4 ps 1.2 lc rgb '#c0392b' t 'scikit-fem SuperLU'
