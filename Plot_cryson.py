import sys, os
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt




ex = []; 
ey = []; 
er = []; 

x,y = np.loadtxt("900.fit", skiprows=1, usecols=(0,2), unpack=True); 
#ex,ey = np.loadtxt("/home/xov/mdmx/SANS/Exp/MX53.dat", skiprows=1, usecols=(0,1), unpack=True)
f = open("/home/xov/mdmx/SANS/Exp/MX53.dat"); 
for line in f.readlines():
    if line.startswith('#'):
        print "skip"
    else:
        l = line.strip(',').split(','); 
        print l; 
        ex.append(float(l[0])); 
        ey.append(float(l[1]));
        er.append(float(l[2]));
        
print len(ex); 
print (x); 
print ex; 


plt.loglog(x, y);
plt.errorbar(ex, ey, er) 
plt.loglog(ex, ey);
plt.xlim([0, 0.5]);  

plt.show(); 


