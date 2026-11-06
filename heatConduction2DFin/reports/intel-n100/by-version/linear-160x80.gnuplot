set terminal pngcairo size 1000,640 font 'Arial,13'
set output 'linear-160x80.png'
set title "FEAScript speed-up by version\n{/*0.75 2D fin heat conduction, 160×80 linear quads (13,041 nodes) · Intel(R) N100, 1 core, Node v18.19.1}" font 'Arial,16'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid ytics lc rgb '#e6e6e6'
set boxwidth 0.315
set xrange [-0.6:2.6]; set yrange [0:52.29]; set xtics scale 0
set ylabel 'Speed-up (assembly + solve), × the first version'; set xlabel 'FEAScript version'
set key top left box lc rgb '#cccccc' opaque
set bmargin 5
set label "Each version was run at a different time; small differences can come from variation in the machine's speed" at screen 0.5,0.03 center tc rgb '#777777' font ',11'
set label "Relative to the first version each solver ran in: frontal vs 0.3.1; sparse LU vs 0.2.0" at graph 0.99,0.97 right tc rgb '#777777' font ',11'
set arrow from graph 0, first 1 to graph 1, first 1 nohead dt 2 lc rgb '#999999'
set label "Sparse matrix assembly (0.3.0, #99)" at 1,33.38 center offset 0,4.3 tc rgb '#2a78d6' font ',11'
set label "Frontal solver fix (0.4.0, #121)" at 2,36.07 center offset 0,4.3 tc rgb '#eb6834' font ',11'
set label 'out of memory' at -0.17,1.046 rotate by 90 left tc rgb '#eb6834' font ',11'
plot 'linear-160x80.dat' u ($0-0.175):2:xtic(1) w boxes fs solid noborder lc rgb '#eb6834' t 'frontal', \
     'linear-160x80.dat' u ($0+0.175):4 w boxes fs solid noborder lc rgb '#2a78d6' t 'sparse LU', \
     '' u ($0-0.175):2:(sprintf($2 < 10 ? '{/:Bold %.1f×}\n%.2f s' : '{/:Bold %.0f×}\n%.2f s',$2,$3)) w labels offset 0,1.6 tc rgb '#333333' font ',11' notitle, \
     '' u ($0+0.175):4:(sprintf($4 < 10 ? '{/:Bold %.1f×}\n%.2f s' : '{/:Bold %.0f×}\n%.2f s',$4,$5)) w labels offset 0,1.6 tc rgb '#333333' font ',11' notitle
