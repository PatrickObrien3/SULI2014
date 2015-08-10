"""
nonnormalized kratky plot first


author: Patrick O'Brien
"""


import os, sys
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

a1 = []; 
b=1; 
li = [];
for i in xrange(1, 3):
    x,y=np.loadtxt(str(i) + '.txt', usecols=(0,1), unpack=True); 
    if b==1:
        li.append(i); 
        #x3.append(float(x)); 
        a1 = np.column_stack((x,y));
        #print a.shape; 
        #print a;  
        b=2; 
    else: 
        a1=np.column_stack((a1,y)); 
        li.append(i);



yval = []
yerr = []; 

for i in xrange(1, 11):
    #print i; 
    #print a[int(i)-1,1:]; 
    r = np.average(a1[int(i)-1, 1:]);
    #print r; 
    s = np.std(a1[int(i)-1, 1:]); 
    #print s; 
    yval.append(float(r)); 
    yerr.append(float(s)); 

aI0 = 0.0063744
hI0 = 0.029555

yval3= []

for j in xrange(1, 11):
    print str(j); 
    ynew = (((float(x[int(j)])**2)*(float(yval[int(j)])))/(aI0))
    yval3.append(float(ynew)); 

print len(yval3); 
print len(x);     
            
plt.plot(x, yval3); 
plt.show();     






