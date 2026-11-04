set terminal pngcairo size 900,620 font 'Arial,13'
set output 'original_case.png'
set title 'Original case, 77x39 linear quads (3120 nodes): end-to-end time (FEAScript 0.4.0-rc)' font 'Arial,14'
set border 3 lc rgb '#888888'; set tics nomirror; set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set boxwidth 0.6; set bmargin 7; set xrange [-0.6:4.6]; set ylabel 'Time (s)'; set yrange [0:3.2]; set xtics rotate by -25
set key top left box lc rgb '#cccccc' opaque
plot 'original_case.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
