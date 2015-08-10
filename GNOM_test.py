"""

script to run GNOM on data from CRYSON

Author: Patrick O'Brien
Date: 8/6/14
"""


import sys, os
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt

hx=np.loadtxt('hxf.txt' ); 
yvalh1=np.loadtxt('yvalh1f.txt'  ); 
yerrh1=np.loadtxt('yerrh1f.txt' ); 

ax=np.loadtxt('axf.txt'  ); 
yvala1=np.loadtxt('yvala1f.txt' ); 
yerra1=np.loadtxt('yerra1f.txt'); 

print ax.shape; 
#print ax; 
print yvala1.shape; 
w = np.array([ax, yvala1]); 
print w.shape;
print w; 

MDapo = np.column_stack([ax, yvala1.T]); 
MDholo = np.column_stack([hx, yvalh1.T]); 


np.savetxt('MDapo.dat', MDapo); 
np.savetxt('MDholo.dat', MDholo); 
    





 
