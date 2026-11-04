set terminal pngcairo size 900,600 font 'Arial,13'
set output 'linear-160x80.png'
set title "FEAScript assembly + solve time by version\n{/*0.75 2D fin heat conduction, 160×80 linear quads (13,041 nodes) · Intel(R) N100, 1 core, Node v18.19.1}" font 'Arial,16'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid ytics lc rgb '#e6e6e6'
set style data histograms; set style histogram clustered gap 1.5
set style fill solid border rgb 'white'; set boxwidth 0.9
set ylabel 'Time (s)'; set xlabel 'FEAScript version'; set yrange [0:1.581]
set key top right box lc rgb '#cccccc' opaque
plot 'linear-160x80.dat' u 3:xtic(1) t 'frontal' lc rgb '#eb6834', \
     '' u 4 t 'sparse LU' lc rgb '#2a78d6', \
     '' u ($0-0.15):3:(sprintf('%.2f s',$3)) w labels offset 0,0.8 tc rgb '#333333' notitle, \
     '' u ($0+0.15):4:(sprintf('%.2f s',$4)) w labels offset 0,0.8 tc rgb '#333333' notitle
