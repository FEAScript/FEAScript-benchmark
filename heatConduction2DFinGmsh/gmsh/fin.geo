// 2D fin, 4 x 2. Meshed by benchmark.py with: gmsh fin.geo -2 -setnumber h <size> -setnumber quads <0|1> -setnumber degree <1|2> -format msh41 -o <mesh>
SetFactory("Built-in");
If (!Exists(h)) h = 0.1; EndIf
If (!Exists(quads)) quads = 0; EndIf
If (!Exists(degree)) degree = 1; EndIf
Point(1) = {0, 0, 0, h}; Point(2) = {4, 0, 0, h}; Point(3) = {4, 2, 0, h}; Point(4) = {0, 2, 0, h};
Line(1) = {1, 2}; Line(2) = {4, 1}; Line(3) = {3, 4}; Line(4) = {2, 3};
Curve Loop(1) = {1, 4, 3, 2};
Plane Surface(1) = {1};
Physical Curve("bottom", 1) = {1};
Physical Curve("left", 2) = {2};
Physical Curve("top", 3) = {3};
Physical Curve("right", 4) = {4};
Physical Surface("domain", 5) = {1};
Mesh.Algorithm = 6;
// Quadrilaterals: split every triangle into three. This needs no recombination, which crashes some Gmsh builds
If (quads)
  Mesh.SubdivisionAlgorithm = 1;
EndIf
Mesh.ElementOrder = degree;
Mesh.SecondOrderIncomplete = 0;
