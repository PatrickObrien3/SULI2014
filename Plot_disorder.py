"""
Plot script to plot the disorder of a sequence as determined by DisorderPredict: Predisorder
from Missouri

Author: Patrick O'Brien
Date: 8/4/14
"""

import sys, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt

dis = []; 
f = open('/home/xov/mdmx/disorder/disorder.txt'); 

for line in f.readlines(): 
    l = line.strip().split(); 
    dis.append(float(l[2])); 
    
print dis; 
x = []; 
for i in xrange(1, len(dis)+1): 
    print i;
    x.append(int(i)); 
print len(dis); 
print len(x); 

dis2 = []; 
g = open('/home/xov/mdmx/disorder/disorder2.txt'); 
for line in g.readlines():
    l = line.strip().split();
    dis2.append(float(l[1])); 





plt.plot(x, dis2, color='k'); 
#plt.plot(x, dis, color='r'); 
plt.title('p53 Disorder Probability vs. Residue Number'); 
plt.xlabel('Disorder Probability'); 
plt.ylabel('Residue Number');
plt.ylim([0.3, 1]);  
plt.show(); 

















