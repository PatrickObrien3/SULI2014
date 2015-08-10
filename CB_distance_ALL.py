import MDAnalysis
from MDAnalysis import *
from MDAnalysis.analysis import *

import sys
import numpy 
import scipy
import sys, os
from MDAnalysis.analysis.distances import *


u = Universe(sys.argv[1], sys.argv[2]);

Dist_4_7 = [];  
Dist_4_8 = []; 
Dist_4_9 = []; 
Dist_4_10 = []; 
Dist_4_11 = []; 
Dist_4_12 = []; 
Dist_4_21 = [];
Dist_4_22 = [];
Dist_4_23 = []; 
Dist_4_24 = []; 
Dist_4_25 = [];
Dist_4_26 = []; 
Dist_4_27 = []; 
Dist_4_31 = []; 
Dist_4_34 = []; 
Dist_4_35 = []; 
Dist_4_36 = []; 
Dist_7_9 = [];
Dist_7_10 = [];
Dist_7_11 = []; 
Dist_7_12 = [];
Dist_7_21 = []; 
Dist_7_22 = []; 
Dist_7_23 = []; 
Dist_7_24 = []; 
Dist_7_25 = [];
Dist_7_26 = [];
Dist_7_27 = []; 
Dist_7_31 = []; 
Dist_7_34 = []; 
Dist_7_35 = []; 
Dist_7_36 = []; 
Dist_8_10 = []; 
Dist_8_11 = []; 
Dist_8_12 = []; 
Dist_8_21 = []; 
Dist_8_22 = []; 
Dist_8_23 = []; 
Dist_8_24 = []; 
Dist_8_25 = []; 
Dist_8_26 = []; 
Dist_8_27 = []; 
Dist_8_31 = []; 
Dist_8_34 = []; 
Dist_8_35 = []; 
Dist_8_36 = []; 
Dist_9_11 = []; 
Dist_9_12 = []; 
Dist_9_21 = []; 
Dist_9_22 = []; 
Dist_9_23 = []; 
Dist_9_24 = [];
Dist_9_25 = []; 
Dist_9_26 = []; 
Dist_9_27 = []; 
Dist_9_31 = []; 
Dist_9_34 = []; 
Dist_9_35 = []; 
Dist_9_36 = []; 
Dist_10_12 = []; 
Dist_10_21 = []; 
Dist_10_22 = []; 
Dist_10_23 = []; 
Dist_10_24 = []; 
Dist_10_25 = []; 
Dist_10_26 = []; 
Dist_10_27 = []; 
Dist_10_31 = []; 
Dist_10_34 = []; 
Dist_10_35 = []; 
Dist_10_36 = []; 
Dist_11_21 = []; 
Dist_11_22 = []; 
Dist_11_23 = []; 
Dist_11_24 = []; 
Dist_11_25 = []; 
Dist_11_26 = []; 
Dist_11_27 = []; 
Dist_11_31 = []; 
Dist_11_34 = []; 
Dist_11_35 = [];
Dist_11_36 = []; 
Dist_12_21 = []; 
Dist_12_22 = []; 
Dist_12_23 = []; 
Dist_12_24 = [];
Dist_12_25 = []; 
Dist_12_26 = []; 
Dist_12_27 = []; 
Dist_12_31 = []; 
Dist_12_34 = []; 
Dist_12_35 = []; 
Dist_12_36 = []; 
Dist_21_23 = []; 
Dist_21_24 = []; 
Dist_21_25 = []; 
Dist_21_26 = []; 
Dist_21_27 = []; 
Dist_21_31 = []; 
Dist_21_34 = []; 
Dist_21_35 = []; 
Dist_21_36 = []; 
Dist_22_24 = []; 
Dist_22_25 = []; 
Dist_22_26 = []; 
Dist_22_27 = [];
Dist_22_31 = [];
Dist_22_34 = []; 
Dist_22_35 = [];
Dist_22_36 = []; 
Dist_23_25 = []; 
Dist_23_26 = []; 
Dist_23_27 = [];
Dist_23_31 = [];
Dist_23_34 = []; 
Dist_23_35 = []; 
Dist_23_36 = []; 
Dist_24_26 = []; 
Dist_24_27 = [];
Dist_24_31 = []; 
Dist_24_34 = [];
Dist_24_35 = []; 
Dist_24_36 = []; 
Dist_25_27 = []; 
Dist_25_31 = []; 
Dist_25_34 = []; 
Dist_25_35 = []; 
Dist_25_36 = []; 
Dist_26_31 = []; 
Dist_26_34 = []; 
Dist_26_35 = []; 
Dist_26_36 = []; 
Dist_27_31 = []; 
Dist_27_34 = []; 
Dist_27_35 = []; 
Dist_27_36 = []; 
Dist_31_34 = []; 
Dist_31_35 = []; 
Dist_31_36 = [];
Dist_34_36 = [];


for ts in u.trajectory:     
	CB4 = u.selectAtoms("resid 4 and name CB");
        CB7 = u.selectAtoms("resid 7 and name CB");
        CB8 = u.selectAtoms("resid 8 and name CB"); 
        CB9 = u.selectAtoms("resid 9 and name CB"); 
        CB10 = u.selectAtoms("resid 10 and name CB"); 
        CB11 = u.selectAtoms("resid 11 and name CB"); 
        CB12 = u.selectAtoms("resid 12 and name CB"); 
        CB21 = u.selectAtoms("resid 21 and name CB"); 
        CB22 = u.selectAtoms("resid 22 and name CB"); 
        CB23 = u.selectAtoms("resid 23 and name CB"); 
        CB24 = u.selectAtoms("resid 24 and name CB"); 
        CB25 = u.selectAtoms("resid 25 and name CB"); 
        CB26 = u.selectAtoms("resid 26 and name CB"); 
        CB27 = u.selectAtoms("resid 27 and name CB");
        CB31 = u.selectAtoms("resid 31 and name CB"); 
        CB34 = u.selectAtoms("resid 34 and name CB"); 
        CB35 = u.selectAtoms("resid 35 and name CB"); 
        CB36 = u.selectAtoms("resid 36 and name CB");  
	Dist_4_7.append(MDAnalysis.analysis.distances.dist(CB4, CB7)[2]);
        Dist_4_8.append(MDAnalysis.analysis.distances.dist(CB4, CB8)[2]);
        Dist_4_9.append(MDAnalysis.analysis.distances.dist(CB4, CB9)[2]);
        Dist_4_10.append(MDAnalysis.analysis.distances.dist(CB4, CB10)[2]);
        Dist_4_11.append(MDAnalysis.analysis.distances.dist(CB4, CB11)[2])
        Dist_4_12.append(MDAnalysis.analysis.distances.dist(CB4, CB12)[2]);    
        Dist_4_21.append(MDAnalysis.analysis.distances.dist(CB4, CB21)[2]);
        Dist_4_22.append(MDAnalysis.analysis.distances.dist(CB4, CB22)[2]);
        Dist_4_23.append(MDAnalysis.analysis.distances.dist(CB4, CB23)[2]);
        Dist_4_24.append(MDAnalysis.analysis.distances.dist(CB4, CB24)[2]);
        Dist_4_25.append(MDAnalysis.analysis.distances.dist(CB4, CB25)[2]);
        Dist_4_26.append(MDAnalysis.analysis.distances.dist(CB4, CB26)[2]);
        Dist_4_27.append(MDAnalysis.analysis.distances.dist(CB4, CB27)[2]);
        Dist_4_31.append(MDAnalysis.analysis.distances.dist(CB4, CB31)[2]);
        Dist_4_34.append(MDAnalysis.analysis.distances.dist(CB4, CB34)[2]);
        Dist_4_35.append(MDAnalysis.analysis.distances.dist(CB4, CB35)[2]);
        Dist_4_36.append(MDAnalysis.analysis.distances.dist(CB4, CB36)[2]);
        Dist_7_9.append(MDAnalysis.analysis.distances.dist(CB7, CB9)[2]);
        Dist_7_10.append(MDAnalysis.analysis.distances.dist(CB7, CB10)[2]);
        Dist_7_11.append(MDAnalysis.analysis.distances.dist(CB7, CB11)[2]);
        Dist_7_12.append(MDAnalysis.analysis.distances.dist(CB7, CB12)[2]);
        Dist_7_21.append(MDAnalysis.analysis.distances.dist(CB7, CB21)[2]);
        Dist_7_22.append(MDAnalysis.analysis.distances.dist(CB7, CB22)[2]);
        Dist_7_23.append(MDAnalysis.analysis.distances.dist(CB7, CB23)[2]);
        Dist_7_24.append(MDAnalysis.analysis.distances.dist(CB7, CB24)[2]);
        Dist_7_25.append(MDAnalysis.analysis.distances.dist(CB7, CB25)[2]);
        Dist_7_26.append(MDAnalysis.analysis.distances.dist(CB7, CB26)[2]);
        Dist_7_27.append(MDAnalysis.analysis.distances.dist(CB7, CB27)[2]);        
        Dist_7_31.append(MDAnalysis.analysis.distances.dist(CB7, CB31)[2]);
        Dist_7_34.append(MDAnalysis.analysis.distances.dist(CB7, CB34)[2]);
        Dist_7_35.append(MDAnalysis.analysis.distances.dist(CB7, CB35)[2]);
        Dist_7_36.append(MDAnalysis.analysis.distances.dist(CB7, CB36)[2]);
        Dist_8_10.append(MDAnalysis.analysis.distances.dist(CB8, CB10)[2]);
        Dist_8_11.append(MDAnalysis.analysis.distances.dist(CB8, CB11)[2]);
        Dist_8_12.append(MDAnalysis.analysis.distances.dist(CB8, CB12)[2]);
        Dist_8_21.append(MDAnalysis.analysis.distances.dist(CB8, CB21)[2]);
        Dist_8_22.append(MDAnalysis.analysis.distances.dist(CB8, CB22)[2]);
        Dist_8_23.append(MDAnalysis.analysis.distances.dist(CB8, CB23)[2]);
        Dist_8_24.append(MDAnalysis.analysis.distances.dist(CB8, CB24)[2]);
        Dist_8_25.append(MDAnalysis.analysis.distances.dist(CB8, CB25)[2]);
        Dist_8_26.append(MDAnalysis.analysis.distances.dist(CB8, CB26)[2]);
        Dist_8_27.append(MDAnalysis.analysis.distances.dist(CB8, CB27)[2]);
        Dist_8_31.append(MDAnalysis.analysis.distances.dist(CB8, CB31)[2]);
        Dist_8_34.append(MDAnalysis.analysis.distances.dist(CB8, CB34)[2]);
        Dist_8_35.append(MDAnalysis.analysis.distances.dist(CB8, CB35)[2]);
        Dist_8_36.append(MDAnalysis.analysis.distances.dist(CB8, CB36)[2]);
        Dist_9_11.append(MDAnalysis.analysis.distances.dist(CB9, CB11)[2]);
        Dist_9_12.append(MDAnalysis.analysis.distances.dist(CB9, CB12)[2]);
        Dist_9_21.append(MDAnalysis.analysis.distances.dist(CB9, CB21)[2]);
        Dist_9_22.append(MDAnalysis.analysis.distances.dist(CB9, CB22)[2]);
        Dist_9_23.append(MDAnalysis.analysis.distances.dist(CB9, CB23)[2]);
        Dist_9_24.append(MDAnalysis.analysis.distances.dist(CB9, CB24)[2]);
        Dist_9_25.append(MDAnalysis.analysis.distances.dist(CB9, CB25)[2]);
        Dist_9_26.append(MDAnalysis.analysis.distances.dist(CB9, CB26)[2]);
        Dist_9_27.append(MDAnalysis.analysis.distances.dist(CB9, CB27)[2]);
        Dist_9_31.append(MDAnalysis.analysis.distances.dist(CB9, CB31)[2]);
        Dist_9_34.append(MDAnalysis.analysis.distances.dist(CB9, CB34)[2]);
        Dist_9_35.append(MDAnalysis.analysis.distances.dist(CB9, CB35)[2]);
        Dist_9_36.append(MDAnalysis.analysis.distances.dist(CB9, CB36)[2]);
        Dist_10_12.append(MDAnalysis.analysis.distances.dist(CB10, CB12)[2]);
        Dist_10_21.append(MDAnalysis.analysis.distances.dist(CB10, CB21)[2]);
        Dist_10_22.append(MDAnalysis.analysis.distances.dist(CB10, CB22)[2]);
        Dist_10_23.append(MDAnalysis.analysis.distances.dist(CB10, CB23)[2]);
        Dist_10_24.append(MDAnalysis.analysis.distances.dist(CB10, CB24)[2]);
        Dist_10_25.append(MDAnalysis.analysis.distances.dist(CB10, CB25)[2]);
        Dist_10_26.append(MDAnalysis.analysis.distances.dist(CB10, CB26)[2]);
        Dist_10_27.append(MDAnalysis.analysis.distances.dist(CB10, CB27)[2]);
        Dist_10_31.append(MDAnalysis.analysis.distances.dist(CB10, CB31)[2]);
        Dist_10_34.append(MDAnalysis.analysis.distances.dist(CB10, CB34)[2]);
        Dist_10_35.append(MDAnalysis.analysis.distances.dist(CB10, CB35)[2]);
        Dist_10_36.append(MDAnalysis.analysis.distances.dist(CB10, CB36)[2]);
        Dist_11_21.append(MDAnalysis.analysis.distances.dist(CB11, CB21)[2]);
        Dist_11_22.append(MDAnalysis.analysis.distances.dist(CB11, CB22)[2]);
        Dist_11_23.append(MDAnalysis.analysis.distances.dist(CB11, CB23)[2]);
        Dist_11_24.append(MDAnalysis.analysis.distances.dist(CB11, CB24)[2]);
        Dist_11_25.append(MDAnalysis.analysis.distances.dist(CB11, CB25)[2]);
        Dist_11_26.append(MDAnalysis.analysis.distances.dist(CB11, CB26)[2]);
        Dist_11_27.append(MDAnalysis.analysis.distances.dist(CB11, CB27)[2]);
        Dist_11_31.append(MDAnalysis.analysis.distances.dist(CB11, CB31)[2]);
        Dist_11_34.append(MDAnalysis.analysis.distances.dist(CB11, CB34)[2]);
        Dist_11_35.append(MDAnalysis.analysis.distances.dist(CB11, CB35)[2]);
        Dist_11_36.append(MDAnalysis.analysis.distances.dist(CB11, CB36)[2]);
        Dist_12_21.append(MDAnalysis.analysis.distances.dist(CB11, CB21)[2]);
        Dist_12_22.append(MDAnalysis.analysis.distances.dist(CB11, CB22)[2]);
        Dist_12_23.append(MDAnalysis.analysis.distances.dist(CB11, CB23)[2]);
        Dist_12_24.append(MDAnalysis.analysis.distances.dist(CB11, CB24)[2]);
        Dist_12_25.append(MDAnalysis.analysis.distances.dist(CB11, CB25)[2]);
        Dist_12_26.append(MDAnalysis.analysis.distances.dist(CB11, CB26)[2]);
        Dist_12_27.append(MDAnalysis.analysis.distances.dist(CB11, CB27)[2]);
        Dist_12_31.append(MDAnalysis.analysis.distances.dist(CB11, CB31)[2]);
        Dist_12_34.append(MDAnalysis.analysis.distances.dist(CB11, CB34)[2]);
        Dist_12_35.append(MDAnalysis.analysis.distances.dist(CB11, CB35)[2]);
        Dist_12_36.append(MDAnalysis.analysis.distances.dist(CB11, CB36)[2]);
        Dist_21_23.append(MDAnalysis.analysis.distances.dist(CB21, CB23)[2]);
        Dist_21_24.append(MDAnalysis.analysis.distances.dist(CB21, CB24)[2]);
        Dist_21_25.append(MDAnalysis.analysis.distances.dist(CB21, CB25)[2]);
        Dist_21_26.append(MDAnalysis.analysis.distances.dist(CB21, CB26)[2]);
        Dist_21_27.append(MDAnalysis.analysis.distances.dist(CB21, CB27)[2]);
        Dist_21_31.append(MDAnalysis.analysis.distances.dist(CB21, CB31)[2]);
        Dist_21_34.append(MDAnalysis.analysis.distances.dist(CB21, CB34)[2]);
        Dist_21_35.append(MDAnalysis.analysis.distances.dist(CB21, CB35)[2]);
        Dist_21_36.append(MDAnalysis.analysis.distances.dist(CB21, CB36)[2]);
        Dist_22_24.append(MDAnalysis.analysis.distances.dist(CB22, CB24)[2]);
        Dist_22_25.append(MDAnalysis.analysis.distances.dist(CB22, CB25)[2]);
        Dist_22_26.append(MDAnalysis.analysis.distances.dist(CB22, CB26)[2]);
        Dist_22_27.append(MDAnalysis.analysis.distances.dist(CB22, CB27)[2]);
        Dist_22_31.append(MDAnalysis.analysis.distances.dist(CB22, CB31)[2]);
        Dist_22_34.append(MDAnalysis.analysis.distances.dist(CB22, CB34)[2]);
        Dist_22_35.append(MDAnalysis.analysis.distances.dist(CB22, CB35)[2]);
        Dist_22_36.append(MDAnalysis.analysis.distances.dist(CB22, CB36)[2]);
        Dist_23_25.append(MDAnalysis.analysis.distances.dist(CB23, CB25)[2]);
        Dist_23_26.append(MDAnalysis.analysis.distances.dist(CB23, CB26)[2]);
        Dist_23_27.append(MDAnalysis.analysis.distances.dist(CB23, CB27)[2]);
        Dist_23_31.append(MDAnalysis.analysis.distances.dist(CB23, CB31)[2]);
        Dist_23_34.append(MDAnalysis.analysis.distances.dist(CB23, CB34)[2]);
        Dist_23_35.append(MDAnalysis.analysis.distances.dist(CB23, CB35)[2]);
        Dist_23_36.append(MDAnalysis.analysis.distances.dist(CB23, CB36)[2]);
        Dist_24_26.append(MDAnalysis.analysis.distances.dist(CB24, CB26)[2]);
        Dist_24_27.append(MDAnalysis.analysis.distances.dist(CB24, CB27)[2]);
        Dist_24_31.append(MDAnalysis.analysis.distances.dist(CB24, CB31)[2]);
        Dist_24_35.append(MDAnalysis.analysis.distances.dist(CB24, CB35)[2]);
        Dist_24_34.append(MDAnalysis.analysis.distances.dist(CB24, CB34)[2]); 
        Dist_24_36.append(MDAnalysis.analysis.distances.dist(CB24, CB36)[2]);
        Dist_25_27.append(MDAnalysis.analysis.distances.dist(CB25, CB27)[2]);
        Dist_25_31.append(MDAnalysis.analysis.distances.dist(CB25, CB31)[2]);
        Dist_25_34.append(MDAnalysis.analysis.distances.dist(CB25, CB34)[2]);
        Dist_25_35.append(MDAnalysis.analysis.distances.dist(CB25, CB35)[2]);
        Dist_25_36.append(MDAnalysis.analysis.distances.dist(CB25, CB36)[2]);
        Dist_26_31.append(MDAnalysis.analysis.distances.dist(CB26, CB31)[2]);
        Dist_26_34.append(MDAnalysis.analysis.distances.dist(CB26, CB34)[2]);
        Dist_26_35.append(MDAnalysis.analysis.distances.dist(CB26, CB35)[2]);
        Dist_26_36.append(MDAnalysis.analysis.distances.dist(CB26, CB36)[2]);
        Dist_27_31.append(MDAnalysis.analysis.distances.dist(CB27, CB31)[2]);
        Dist_27_34.append(MDAnalysis.analysis.distances.dist(CB27, CB34)[2]);
        Dist_27_35.append(MDAnalysis.analysis.distances.dist(CB27, CB35)[2]);
        Dist_27_36.append(MDAnalysis.analysis.distances.dist(CB27, CB36)[2]);
        Dist_31_34.append(MDAnalysis.analysis.distances.dist(CB31, CB34)[2]);
        Dist_31_35.append(MDAnalysis.analysis.distances.dist(CB31, CB35)[2]);
        Dist_31_36.append(MDAnalysis.analysis.distances.dist(CB31, CB36)[2]);
        Dist_34_36.append(MDAnalysis.analysis.distances.dist(CB34, CB36)[2]);






numpy.savetxt('Dist4_7.txt', Dist_4_7 , delimiter=',');
numpy.savetxt('Dist4_8.txt', Dist_4_8, delimiter=',');
numpy.savetxt('Dist4_9.txt', Dist_4_9, delimiter=',');
numpy.savetxt('Dist4_10.txt', Dist_4_10, delimiter=',');
numpy.savetxt('Dist4_11.txt', Dist_4_11, delimiter=',');
numpy.savetxt('Dist4_12.txt', Dist_4_12, delimiter=',');
numpy.savetxt('Dist4_21.txt', Dist_4_21, delimiter=',');
numpy.savetxt('Dist4_22.txt', Dist_4_22, delimiter=',');
numpy.savetxt('Dist4_23.txt', Dist_4_23, delimiter=',');
numpy.savetxt('Dist4_24.txt', Dist_4_24, delimiter=',');
numpy.savetxt('Dist4_25.txt', Dist_4_25, delimiter=',');
numpy.savetxt('Dist4_26.txt', Dist_4_26, delimiter=',');
numpy.savetxt('Dist4_27.txt', Dist_4_27, delimiter=',');
numpy.savetxt('Dist4_31.txt', Dist_4_31, delimiter=',');
numpy.savetxt('Dist4_34.txt', Dist_4_34, delimiter=',');
numpy.savetxt('Dist4_35.txt', Dist_4_35, delimiter=',');
numpy.savetxt('Dist4_36.txt', Dist_4_36, delimiter=',');
numpy.savetxt('Dist7_9.txt', Dist_7_9, delimiter=',');
numpy.savetxt('Dist7_10.txt', Dist_7_10, delimiter=',');
numpy.savetxt('Dist7_11.txt', Dist_7_11, delimiter=',');
numpy.savetxt('Dist7_12.txt', Dist_7_12, delimiter=',');
numpy.savetxt('Dist7_21.txt', Dist_7_21, delimiter=',');
numpy.savetxt('Dist7_22.txt', Dist_7_22, delimiter=',');
numpy.savetxt('Dist7_23.txt', Dist_7_23, delimiter=',');
numpy.savetxt('Dist7_24.txt', Dist_7_24, delimiter=',');
numpy.savetxt('Dist7_25.txt', Dist_7_25, delimiter=',');
numpy.savetxt('Dist7_26.txt', Dist_7_26, delimiter=',');
numpy.savetxt('Dist7_27.txt', Dist_7_27, delimiter=',');
numpy.savetxt('Dist7_31.txt', Dist_7_31, delimiter=',');
numpy.savetxt('Dist7_34.txt', Dist_7_34, delimiter=',');
numpy.savetxt('Dist7_35.txt', Dist_7_35, delimiter=',');
numpy.savetxt('Dist7_36.txt', Dist_7_36, delimiter=',');
numpy.savetxt('Dist8_10.txt', Dist_8_10, delimiter=',');
numpy.savetxt('Dist8_11.txt', Dist_8_11, delimiter=',');
numpy.savetxt('Dist8_12.txt', Dist_8_12, delimiter=',');
numpy.savetxt('Dist8_21.txt', Dist_8_21, delimiter=',');
numpy.savetxt('Dist8_22.txt', Dist_8_22, delimiter=',');
numpy.savetxt('Dist8_23.txt', Dist_8_23, delimiter=',');
numpy.savetxt('Dist8_24.txt', Dist_8_24, delimiter=',');
numpy.savetxt('Dist8_25.txt', Dist_8_25, delimiter=',');
numpy.savetxt('Dist8_26.txt', Dist_8_26, delimiter=',');
numpy.savetxt('Dist8_27.txt', Dist_8_27, delimiter=',');
numpy.savetxt('Dist8_31.txt', Dist_8_31, delimiter=',');
numpy.savetxt('Dist8_34.txt', Dist_8_34, delimiter=',');
numpy.savetxt('Dist8_35.txt', Dist_8_35, delimiter=',');
numpy.savetxt('Dist8_36.txt', Dist_8_36, delimiter=',');
numpy.savetxt('Dist9_11.txt', Dist_9_11, delimiter=',');
numpy.savetxt('Dist9_12.txt', Dist_9_12, delimiter=',');
numpy.savetxt('Dist9_21.txt', Dist_9_21, delimiter=',');
numpy.savetxt('Dist9_22.txt', Dist_9_22, delimiter=',');
numpy.savetxt('Dist9_23.txt', Dist_9_23, delimiter=',');
numpy.savetxt('Dist9_24.txt', Dist_9_24, delimiter=',');
numpy.savetxt('Dist9_25.txt', Dist_9_25, delimiter=',');
numpy.savetxt('Dist9_26.txt', Dist_9_26, delimiter=',');
numpy.savetxt('Dist9_27.txt', Dist_9_27, delimiter=',');
numpy.savetxt('Dist9_31.txt', Dist_9_31, delimiter=',');
numpy.savetxt('Dist9_34.txt', Dist_9_34, delimiter=',');
numpy.savetxt('Dist9_35.txt', Dist_9_35, delimiter=',');
numpy.savetxt('Dist9_36.txt', Dist_9_36, delimiter=',');
numpy.savetxt('Dist10_12.txt', Dist_10_12, delimiter=',');
numpy.savetxt('Dist10_21.txt', Dist_10_21, delimiter=',');
numpy.savetxt('Dist10_22.txt', Dist_10_22, delimiter=',');
numpy.savetxt('Dist10_23.txt', Dist_10_23, delimiter=',');
numpy.savetxt('Dist10_24.txt', Dist_10_24, delimiter=',');
numpy.savetxt('Dist10_25.txt', Dist_10_25, delimiter=',');
numpy.savetxt('Dist10_26.txt', Dist_10_26, delimiter=',');
numpy.savetxt('Dist10_27.txt', Dist_10_27, delimiter=',');
numpy.savetxt('Dist10_31.txt', Dist_10_31, delimiter=',');
numpy.savetxt('Dist10_34.txt', Dist_10_34, delimiter=',');
numpy.savetxt('Dist10_35.txt', Dist_10_35, delimiter=',');
numpy.savetxt('Dist10_36.txt', Dist_10_36, delimiter=',');
numpy.savetxt('Dist11_21.txt', Dist_11_21, delimiter=',');
numpy.savetxt('Dist11_22.txt', Dist_11_22, delimiter=',');
numpy.savetxt('Dist11_23.txt', Dist_11_23, delimiter=',');
numpy.savetxt('Dist11_24.txt', Dist_11_24, delimiter=',');
numpy.savetxt('Dist11_25.txt', Dist_11_25, delimiter=',');
numpy.savetxt('Dist11_26.txt', Dist_11_26, delimiter=',');
numpy.savetxt('Dist11_27.txt', Dist_11_27, delimiter=',');
numpy.savetxt('Dist11_31.txt', Dist_11_31, delimiter=',');
numpy.savetxt('Dist11_34.txt', Dist_11_34, delimiter=',');
numpy.savetxt('Dist11_35.txt', Dist_11_35, delimiter=',');
numpy.savetxt('Dist11_36.txt', Dist_11_36, delimiter=',');
numpy.savetxt('Dist12_21.txt', Dist_12_21, delimiter=',');
numpy.savetxt('Dist12_22.txt', Dist_12_22, delimiter=',');
numpy.savetxt('Dist12_23.txt', Dist_12_23, delimiter=',');
numpy.savetxt('Dist12_24.txt', Dist_12_24, delimiter=',');
numpy.savetxt('Dist12_25.txt', Dist_12_25, delimiter=',');
numpy.savetxt('Dist12_26.txt', Dist_12_26, delimiter=',');
numpy.savetxt('Dist12_27.txt', Dist_12_27, delimiter=',');
numpy.savetxt('Dist12_31.txt', Dist_12_31, delimiter=',');
numpy.savetxt('Dist12_34.txt', Dist_12_34, delimiter=',');
numpy.savetxt('Dist12_35.txt', Dist_12_35, delimiter=',');
numpy.savetxt('Dist12_36.txt', Dist_12_36, delimiter=',');
numpy.savetxt('Dist21_23.txt', Dist_21_23, delimiter=',');
numpy.savetxt('Dist21_24.txt', Dist_21_24, delimiter=',');
numpy.savetxt('Dist21_25.txt', Dist_21_25, delimiter=',');
numpy.savetxt('Dist21_26.txt', Dist_21_26, delimiter=',');
numpy.savetxt('Dist21_27.txt', Dist_21_27, delimiter=',');
numpy.savetxt('Dist21_31.txt', Dist_21_31, delimiter=',');
numpy.savetxt('Dist21_34.txt', Dist_21_34, delimiter=',');
numpy.savetxt('Dist21_35.txt', Dist_21_35, delimiter=',');
numpy.savetxt('Dist21_36.txt', Dist_21_36, delimiter=',');
numpy.savetxt('Dist22_24.txt', Dist_22_24, delimiter=',');
numpy.savetxt('Dist22_25.txt', Dist_22_25, delimiter=',');
numpy.savetxt('Dist22_26.txt', Dist_22_26, delimiter=',');
numpy.savetxt('Dist22_27.txt', Dist_22_27, delimiter=',');
numpy.savetxt('Dist22_31.txt', Dist_22_31, delimiter=',');
numpy.savetxt('Dist22_34.txt', Dist_22_34, delimiter=',');
numpy.savetxt('Dist22_35.txt', Dist_22_35, delimiter=',');
numpy.savetxt('Dist22_36.txt', Dist_22_36, delimiter=',');
numpy.savetxt('Dist23_25.txt', Dist_23_25, delimiter=',');
numpy.savetxt('Dist23_26.txt', Dist_23_26, delimiter=',');
numpy.savetxt('Dist23_27.txt', Dist_23_27, delimiter=',');
numpy.savetxt('Dist23_31.txt', Dist_23_31, delimiter=',');
numpy.savetxt('Dist23_34.txt', Dist_23_34, delimiter=',');
numpy.savetxt('Dist23_35.txt', Dist_23_35, delimiter=',');
numpy.savetxt('Dist23_36.txt', Dist_23_36, delimiter=',');
numpy.savetxt('Dist24_26.txt', Dist_24_26, delimiter=',');
numpy.savetxt('Dist24_27.txt', Dist_24_27, delimiter=',');
numpy.savetxt('Dist24_31.txt', Dist_24_31, delimiter=',');
numpy.savetxt('Dist24_34.txt', Dist_24_34, delimiter=',');
numpy.savetxt('Dist24_35.txt', Dist_24_35, delimiter=',');
numpy.savetxt('Dist24_36.txt', Dist_24_36, delimiter=',');
numpy.savetxt('Dist25_27.txt', Dist_25_27, delimiter=',');
numpy.savetxt('Dist25_31.txt', Dist_25_31, delimiter=',');
numpy.savetxt('Dist25_34.txt', Dist_25_34, delimiter=',');
numpy.savetxt('Dist25_35.txt', Dist_25_35, delimiter=',');
numpy.savetxt('Dist25_36.txt', Dist_25_36, delimiter=',');
numpy.savetxt('Dist26_31.txt', Dist_26_31, delimiter=',');
numpy.savetxt('Dist26_34.txt', Dist_26_34, delimiter=',');
numpy.savetxt('Dist26_35.txt', Dist_26_35, delimiter=',');
numpy.savetxt('Dist26_36.txt', Dist_26_36, delimiter=',');
numpy.savetxt('Dist27_31.txt', Dist_27_31, delimiter=',');
numpy.savetxt('Dist27_34.txt', Dist_27_34, delimiter=',');
numpy.savetxt('Dist27_35.txt', Dist_27_35, delimiter=',');
numpy.savetxt('Dist27_36.txt', Dist_27_36, delimiter=',');
numpy.savetxt('Dist31_34.txt', Dist_31_34, delimiter=',');
numpy.savetxt('Dist31_35.txt', Dist_31_35, delimiter=',');
numpy.savetxt('Dist31_36.txt', Dist_31_36, delimiter=',');
numpy.savetxt('Dist34_36.txt', Dist_34_36, delimiter=',');

"""
Dist_4_7  

Dist_4_8 

Dist_4_9 

Dist_4_10 
Dist_4_11 
Dist_4_12 
Dist_4_21
Dist_4_22
Dist_4_23 
Dist_4_24 
Dist_4_25
Dist_4_26 
Dist_4_27 
Dist_4_31 
Dist_4_34 
Dist_4_35 
Dist_4_36 


Dist_7_9 
Dist_7_10
Dist_7_11 
Dist_7_12 
Dist_7_21 
Dist_7_22 
Dist_7_23 
Dist_7_24 
Dist_7_25
Dist_7_26
Dist_7_27 
Dist_7_31 
Dist_7_34 
Dist_7_35 
Dist_7_36 


Dist_8_10 
Dist_8_11 
Dist_8_12 
Dist_8_21 
Dist_8_22 
Dist_8_23 
Dist_8_24 
Dist_8_25 
Dist_8_26 
Dist_8_27 
Dist_8_31 
Dist_8_34 
Dist_8_35 
Dist_8_36 


Dist_9_11 
Dist_9_12 
Dist_9_21 
Dist_9_22 
Dist_9_23 
Dist_9_24 
Dist_9_25 
Dist_9_26 
Dist_9_27 
Dist_9_31 
Dist_9_34 
Dist_9_35 
Dist_9_36 


Dist_10_12 
Dist_10_21 
Dist_10_22 
Dist_10_23 
Dist_10_24 
Dist_10_25 
Dist_10_26 
Dist_10_27 
Dist_10_31 
Dist_10_34 
Dist_10_35 
Dist_10_36 


Dist_11_21 
Dist_11_22 
Dist_11_23 
Dist_11_24 
Dist_11_25 
Dist_11_26 
Dist_11_27 
Dist_11_31 
Dist_11_34 
Dist_11_35
Dist_11_36 

Dist_12_21 
Dist_12_22 
Dist_12_23 
Dist_12_24
Dist_12_25 
Dist_12_26 
Dist_12_27 
Dist_12_31 
Dist_12_34 
Dist_12_35 
Dist_12_36 

Dist_21_23 
Dist_21_24 
Dist_21_25 
Dist_21_26 
Dist_21_27 
Dist_21_31 
Dist_21_34 
Dist_21_35 
Dist_21_36 

Dist_22_24 
Dist_22_25 
Dist_22_26 
Dist_22_27 
Dist_22_31 
Dist_22_34 
Dist_22_35
Dist_22_36 

Dist_23_25 
Dist_23_26 
Dist_23_27 
Dist_23_31 
Dist_23_34 
Dist_23_35 
Dist_23_36 

Dist_24_26 
Dist_24_27
Dist_24_31 
Dist_24_34
Dist_24_35 
Dist_24_36 

Dist_25_27 
Dist_25_31 
Dist_25_34 
Dist_25_35 
Dist_25_36 

Dist_26_31 
Dist_26_34 
Dist_26_35 
Dist_26_36 

Dist_27_31 
Dist_27_34 
Dist_27_35 
Dist_27_36 

Dist_31_34 
Dist_31_35 
Dist_31_36 

Dist_34_36 


"""



"""Dist_11-24
referenceCB7 = u.selectAtoms('resid 7 and CB')
selectionCB7 = u.selectAtoms('4 CB, and 9:12 CB, and 21:27 CB, and 31 CB, and 34:36 CB')

referenceCB8 = u.selectAtoms('8 CB')
selectionCB8 = u.selectAtoms('4 CB, and 10:12 CB, and 21:27 CB, and 31 CB, and 34:36 CB ')

referenceCB9 = u.selectAtoms('9 CB')
selectionCB9 = u.selectAtoms('4 CB, and 7 CB, and 11:12 CB, and 21:27 CB, and 31 CB, and 34:36 CB')

referenceCB10 = u.selectAtoms('10 CB')
selectionCB10 = u.selectAtoms('4 CB, and 7:8 CB, and 12 CB, and 21:27 CB, and 31 CB, and 34:36 CB')

referenceCB11 = u.selectAtoms('11 CB')
selectionCB11 = u.selectAtoms('4 CB, and 7:9 CB, and 21:27 CB, and 31 CB, and 34:36 CB')

referenceCB12 = u.selectAtoms('12 CB')
selectionCB12 = u.selectAtoms('4 CB, and 7:10 CB, and 21:27 CB, and 31 CB, and 34:36 CB')

referenceCB21 = u.selectAtoms('21 CB')
selectionCB21 = u.selectAtoms('4 CB and 7:12 CB, and 23:27 CB, and 31 CB, and 34:36 CB')

referenceCB22 = u.selectAtoms('22 CB')
selectionCB22 = u.selectAtoms('4 CB and 7:12 CB, and 31 CB, and 34:36 and 31 CB, and 34:36 CB')

referenceCB23 = u.selectAtoms('23 CB')
selectionCB23 = u.selectAtoms('4 CB and 7:12 CB, and 21 CB, and 25:27 CB, and 31 CB, and 34:36 CB')

referenceCB24 = u.selectAtoms('24 CB')
selectionCB24 = u.selectAtoms('4 CB and 7:12 CB, and 21:22 CB, and 26:27 CB, and 31 CB, and 34:36 CB')

referenceCB25 = u.selectAtoms('25 CB')
selectionCB25 = u.selectAtoms('4 CB and 7:12 CB, and 21:23 CB, and 27 CB, and 31 CB, and 34:36 CB')

referenceCB26 = u.selectAtoms('26 CB')
selectionCB26 = u.selectAtoms('4 CB and 7:12 CB, and 21:24 CB, and 31 CB, and 34:36 CB')

referenceCB27 = u.selectAtoms('27 CB')
selectionCB27 = u.selectAtoms('4 CB and 7:12 CB, and 21:25 CB, and 31 CB, and 34:36 CB')

referenceCB31 = u.selectAtoms('31 CB')
selectionCB31 = u.selectAtoms('4 CB and 7:12 CB, and 21:27 CB, and 34:36 CB')

referenceCB34 = u.selectAtoms('34 CB')
selectionCB34 = u.selectAtoms('4 CB and 7:12 CB, and 21:27 CB, and 31 CB, and 36 CB')

referenceCB35 = u.selectAtoms('35 CB')
selectionCB35 = u.selectAtoms('4 CB and 7:12 CB, and 21:27 CB, and 31 CB')

referenceCB36 = u.selectAtoms('36 CB')
selectionCB36 = u.selectAtoms('4 CB and 7:12 CB,and 21:27 CB, and 31 CB, and 34 CB')

"""