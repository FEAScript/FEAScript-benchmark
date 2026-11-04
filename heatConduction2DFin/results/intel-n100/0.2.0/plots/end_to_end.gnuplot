set terminal pngcairo size 900,620 font 'Arial,13'
set output 'end_to_end.png'
set title 'End-to-end time, 77×39 linear quads (3,120 nodes) (FEAScript 0.2.0, Intel(R) N100)' font 'Arial,14'
set border 3 lc rgb '#888888'; set tics nomirror; set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram rowstacked; set style fill solid border rgb 'white'
set boxwidth 0.6; set bmargin 7; set xrange [-0.6:4.6]; set ylabel 'Time (s)'; set yrange [0:5.17]; set xtics rotate by -25
set key top left box lc rgb '#cccccc' opaque
set label "Elmer runs on one core as one MPI process; most of its time is MPI start-up in this build, not solving" at screen 0.5,0.025 center tc rgb '#777777' font ',11'
plot 'end_to_end.dat' u 2:xtic(1) t 'assembly + solve' lc rgb '#2a78d6', \
     '' u 3 t 'process startup, library load / MPI init, I/O' lc rgb '#b7d3f6'
