set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'end_to_end.png'
set title 'End-to-end time, 16×16 mesh (FEAScript 0.3.1, Intel(R) N100)' font 'Arial,15'
set grid ytics; set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set label "Elmer runs on one core as one MPI process; most of its time is MPI start-up in this build, not solving" at screen 0.5,0.025 center tc rgb '#777777' font ',11'
set boxwidth 0.6; set bmargin 5; set xrange [-0.6:3.6]; set ylabel 'Time (s)'; set yrange [0:3.11]; set key top left box
plot 'end_to_end.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
