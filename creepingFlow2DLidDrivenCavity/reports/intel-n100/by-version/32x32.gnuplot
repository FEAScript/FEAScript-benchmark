set terminal pngcairo size 1000,640 font 'Arial,13'
set output '32x32.png'
set title "FEAScript speed-up by version\n{/*0.75 Lid-driven cavity (Stokes flow), 32×32 Q2–Q1 mesh (4,225 nodes) · Intel(R) N100, 1 core, Node v18.19.1}" font 'Arial,16'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid ytics lc rgb '#e6e6e6'
set boxwidth 0.630
set xrange [-0.6:2.6]; set yrange [0:31.24]; set xtics scale 0
set ylabel 'Speed-up (assembly + solve), × the first version'; set xlabel 'FEAScript version'
set key top left box lc rgb '#cccccc' opaque
set bmargin 5
set label "Each version was run at a different time; small differences can come from variation in the machine's speed" at screen 0.5,0.03 center tc rgb '#777777' font ',11'
set label "Relative to the first version each solver ran in: sparse LU vs 0.2.0" at graph 0.99,0.97 right tc rgb '#777777' font ',11'
set arrow from graph 0, first 1 to graph 1, first 1 nohead dt 2 lc rgb '#999999'
set label "Sparse matrix assembly (0.3.0, #99)" at 1,3.152 center offset 0,4.3 tc rgb '#2a78d6' font ',11'
set label "LU ordering for creeping flow (#132)" at 2,21.55 center offset 0,4.3 tc rgb '#2a78d6' font ',11'
plot '32x32.dat' u ($0+0.000):2:xtic(1) w boxes fs solid noborder lc rgb '#2a78d6' t 'sparse LU', \
     '' u ($0+0.000):2:(sprintf($2 < 10 ? '{/:Bold %.1f×}\n%.2f s' : '{/:Bold %.0f×}\n%.2f s',$2,$3)) w labels offset 0,1.6 tc rgb '#333333' font ',11' notitle
