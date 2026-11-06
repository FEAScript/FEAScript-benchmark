set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'memory.png'
set title 'Peak memory (FEAScript 0.4.0-rc, Intel(R) N100)' font 'Arial,15'
set logscale xy; set format x '10^{%L}'
set xlabel 'Number of nodes (Q2 velocity nodes)'; set ylabel 'Peak memory (MB)'
set label 'Whole process: includes Node.js, Python or Elmer itself' at graph 0.98,0.05 right tc rgb '#777777'
plot 'memory_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 pt 7 ps 1.2 lc rgb '#2a78d6' t 'FEAScript sparse LU', \
     'memory_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 pt 9 ps 1.2 lc rgb '#1baf7a' t 'Elmer UMFPACK', \
     'memory_Elmer_MUMPS.dat' u 1:2 w lp lw 2 pt 13 ps 1.2 lc rgb '#e87ba4' t 'Elmer MUMPS', \
     'memory_scikit_fem_SuperLU.dat' u 1:2 w lp lw 2 pt 4 ps 1.2 lc rgb '#c0392b' t 'scikit-fem SuperLU'
