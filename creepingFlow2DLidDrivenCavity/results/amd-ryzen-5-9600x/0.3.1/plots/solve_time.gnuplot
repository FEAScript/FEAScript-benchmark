set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'solve_time.png'
set title 'Assembly + solve time (FEAScript 0.3.1, AMD Ryzen 5 9600X 6-Core Processor)' font 'Arial,15'
set logscale xy; set format y '10^{%L}'; set format x '10^{%L}'
set xlabel 'Number of nodes (Q2 velocity nodes)'; set ylabel 'Time (s)'
set label 'Elmer timer resolution 0.01 s' at graph 0.98,0.05 right tc rgb '#777777'
plot 'solve_FEAScript_sparse_LU.dat' u 1:2 w lp lw 2 pt 7 ps 1.2 lc rgb '#2a78d6' t 'FEAScript sparse LU', \
     'solve_Elmer_UMFPACK.dat' u 1:2 w lp lw 2 pt 9 ps 1.2 lc rgb '#1baf7a' t 'Elmer UMFPACK', \
     'solve_Elmer_MUMPS.dat' u 1:2 w lp lw 2 pt 13 ps 1.2 lc rgb '#e87ba4' t 'Elmer MUMPS'
