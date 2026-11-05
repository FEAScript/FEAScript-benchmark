set terminal pngcairo size 900,620 font 'Arial,13'
set border 3 lc rgb '#888888'; set tics nomirror tc rgb '#333333'
set grid lc rgb '#e6e6e6' lw 1; set key top left box lc rgb '#cccccc' opaque
set output 'centerline.png'
set title 'Velocity u along the vertical centerline, 64×64 mesh (FEAScript 0.4.0-rc, AMD Ryzen 5 9600X 6-Core Processor)' font 'Arial,14'
set xlabel 'u(0.5, y)'; set ylabel 'y'; set yrange [0:1]; set key bottom right
plot '../../../../elmer/results/amd-ryzen-5-9600x/26.2/centerline_Elmer_UMFPACK_64x64.dat' u 2:1 w l lw 3 lc rgb '#1baf7a' t 'Elmer', \
     '../../../../scikit-fem/results/amd-ryzen-5-9600x/12.0.2/centerline_scikit_fem_SuperLU_64x64.dat' u 2:1 w p pt 4 ps 1.2 lc rgb '#c0392b' t 'scikit-fem', \
     '../../../../feascript/results/amd-ryzen-5-9600x/0.4.0-rc/node/18.19.1/centerline_FEAScript_sparse_LU_64x64.dat' u 2:1 w p pt 7 ps 0.6 lc rgb '#2a78d6' t 'FEAScript'
