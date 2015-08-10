#pair wise rmsd using MDAnalysis

import MDAnalysis
from MDAnalysis import *
import numpy as np
from MDAnalysis.analysis import *
import sys, os
import matplotlib
import matplotlib.pyplot as plt
import pickle

u = Universe(sys.argv[1], sys.argv[2]); 
ca = u.selectAtoms('name CA and (resid 6 or resid 7 or resid 9 or resid 11 or resid 21 or resid 23 or resid 34 or resid 35 or resid 36 or resid 37)')
#selected these residues based on p27

print 'i j rmsd';
numfiles = 10;

testList = [];
#rmsd = np.zeros((numfiles*10, (numfiles2*10)));
m = 0

for i in xrange(m, numfiles):
    for j in xrange(i+1, 50000):
        rmsd = MDAnalysis.analysis.rms.rmsd(ca.coordinates(u.trajectory[i]), ca.coordinates(u.trajectory[j])); 
        #testList.append([str(i+1) + ' ' + str(j+1) + ' ' + str(rmsd)]); 
        print str(i+1) + ' ' + str(j+1) + ' ' + str(rmsd);
        m +=m+1;


"""
m = 1000; 
n = 1010;  

for x in xrange(0, 100):
    print x;
    rmsd = np.zeros((numfiles1, (numfiles2*10))); 
    for i in xrange(m, n):
        for j in xrange(1, numfiles2):
            rmsd[i, j] = MDAnalysis.analysis.rms.rmsd(ca.coordinates(u.trajectory[i]), ca.coordinates(u.trajectory[j]));
            print str(i) + ' ' + str(j) + ' ' + str(rmsd[i][j]);
    m += 10;
    n += 10;


Plot Info
        rmsd[j, i] = rmsd[i, j] #needed to give shape to the other side of plot 
        print str(i)+ ' ' + str(j)+ ' ' + str(rmsd[i][j])
 


plt.pcolor(rmsd)
plt.colorbar()
plt.savefig(filename='pairwise_rmsd_p27.pdf');
plt.show()
"""


"""
Here is the attepmt at different sections, but the array was causing a memory error

numfiles1 = 100;
numfiles2 = 50000;

#rmsd = np.zeros((numfiles1*10, (numfiles2)*10));

#this section provides numbers i 0-999; 

m = 0; 
n = 10;  

for x in xrange(0, 5000):
    rmsd = np.zeros((numfiles1*10, (numfiles2*10))); 
    for i in xrange(m, n):
        for j in xrange(1, numfiles2):
            rmsd[i, j] = MDAnalysis.analysis.rms.rmsd(ca.coordinates(u.trajectory[i]), ca.coordinates(u.trajectory[j]));
            print str(i) + ' ' + str(j) + ' ' + str(rmsd[i][j]);
    m += 10;
    n += 10;
"""
 