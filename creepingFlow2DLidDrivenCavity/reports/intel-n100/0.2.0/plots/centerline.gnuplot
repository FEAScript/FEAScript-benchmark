set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'centerline.png'
set title 'Velocity u along the vertical centerline, 32×32 mesh (FEAScript 0.2.0, Intel(R) N100)' font 'Arial,14'
set xlabel 'u(0.5, y)'; set ylabel 'y'; set yrange [0:1]; set key bottom right
plot '../../../../elmer/results/intel-n100/26.2/centerline_Elmer_UMFPACK_32x32.dat' u 2:1 w l lw 3 lc rgb '#1baf7a' t 'Elmer', \
     '../../../../scikit-fem/results/intel-n100/12.0.2/centerline_scikit_fem_SuperLU_32x32.dat' u 2:1 w p pt 4 ps 1.2 lc rgb '#c0392b' t 'scikit-fem', \
     '../../../../feascript/results/intel-n100/0.2.0/node/18.19.1/centerline_FEAScript_sparse_LU_32x32.dat' u 2:1 w p pt 7 ps 0.6 lc rgb '#2a78d6' t 'FEAScript'
