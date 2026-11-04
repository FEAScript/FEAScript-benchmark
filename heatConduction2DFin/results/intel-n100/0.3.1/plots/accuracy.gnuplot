set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
set output 'accuracy.png'
set title 'RMS nodal error vs exact solution (FEAScript 0.3.1, Intel(R) N100)' font 'Arial,15'
set xlabel 'Number of nodes'
set ylabel 'RMS error (K)'
set key bottom left
set label 'FEAScript and Elmer curves coincide (difference < 1e-5 K)' at graph 0.98,0.95 right tc rgb '#777777'
plot 'err_linear_FEAScript.dat' u 1:2 w lp lw 2 dt 1 pt 7 ps 1.0 lc rgb '#2a78d6' t 'FEAScript (linear)', \
     'err_linear_Elmer.dat' u 1:2 w lp lw 2 dt 1 pt 6 ps 1.6 lc rgb '#1baf7a' t 'Elmer (linear)', \
     'err_quadratic_FEAScript.dat' u 1:2 w lp lw 2 dt 2 pt 7 ps 1.0 lc rgb '#2a78d6' t 'FEAScript (quadratic)', \
     'err_quadratic_Elmer.dat' u 1:2 w lp lw 2 dt 2 pt 6 ps 1.6 lc rgb '#1baf7a' t 'Elmer (quadratic)'
