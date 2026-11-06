set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
set output 'browsers_FEAScript_sparse_LU_linear_quads_repeated.png'
set title 'Repeated solves: FEAScript sparse LU, linear quads (FEAScript 0.4.0-rc, Intel(R) N100)' font 'Arial,12'
set xlabel 'Number of nodes'
set ylabel 'Time (s)'
plot 'browsers_FEAScript_sparse_LU_linear_quads_repeated_node.dat' u 1:2 w lp lw 2 pt 9 ps 1.2 lc rgb '#1baf7a' t 'Node.js', \
     'browsers_FEAScript_sparse_LU_linear_quads_repeated_chromium.dat' u 1:2 w lp lw 2 pt 7 ps 1.2 lc rgb '#2a78d6' t 'Chromium', \
     'browsers_FEAScript_sparse_LU_linear_quads_repeated_firefox.dat' u 1:2 w lp lw 2 pt 5 ps 1.2 lc rgb '#eb6834' t 'Firefox'
