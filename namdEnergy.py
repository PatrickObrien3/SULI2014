#plot for NAMD Energy
# input is namd energy file, with protein selected and 
# All energies computed


import sys, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


EnergyFile = open(sys.argv[1])
frames = []; 
TotalE = []; 







for line in EnergyFile.readlines(): 
    f = line.strip().split(); 
    if f[0] == 'Frame':
        print 'skip';
    else: 
        TotalE.append(float(f[10])); 
        frames.append(float(f[0])); 
        
print len(frames); 
print len(TotalE); 

#plot 

 
plt.plot(frames, TotalE, 'bo', linewidth=0.1, linestyle='-', markevery=750, label='p53 Total Energy'); 
plt.show();  