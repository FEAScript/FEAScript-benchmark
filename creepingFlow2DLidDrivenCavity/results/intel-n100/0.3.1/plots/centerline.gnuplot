set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'centerline.png'
set title 'Velocity u along the vertical centerline, 64×64 mesh (FEAScript 0.3.1, Intel(R) N100)' font 'Arial,14'
set xlabel 'u(0.5, y)'; set ylabel 'y'; set yrange [0:1]; set key bottom right
plot '../work/centerline_Elmer_UMFPACK_64x64.dat' u 2:1 w l lw 3 lc rgb '#1baf7a' t 'Elmer', \
     '../work/centerline_FEAScript_sparse_LU_64x64.dat' u 2:1 w p pt 7 ps 0.6 lc rgb '#2a78d6' t 'FEAScript'
