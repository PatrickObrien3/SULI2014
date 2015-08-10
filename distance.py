#Distances Test for further contact analysis

import MDAnalysis
import numpy as np
import sys, os 
from MDAnalysis import * 
from MDAnalysis.analysis import *
from MDAnalysis.analysis.contacts import *
from MDAnalysis.analysis.distances import *
import itertools 
from itertools import *
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.pyplot import *


u = Universe('/home/xov/mdmx/top_dcd/MDMX_mdm.pdb', '/home/xov/mdmx/top_dcd/mdmh_MDMX.dcd');
d = Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd');
ref = Universe('/home/xov/mdmx/top_dcd/junk_both.pdb'); 
print u; 
print d; 
print ref; 

#Sel1 here is the alpha2 helix
tsel1 = 'name CA and (resid 26 or resid 27 or resid 28 or resid 29 or resid 30 or resid 31 or resid 32 or resid 33 or resid 34 or resid 35 or resid 36 or resid 37 or resid 38 or resid 39 or resid 40 or resid 41 or resid 42 or resid 43)' #actual selection used in calculation
tselp53 = 'name CA and (resid 88 or resid 89 or resid 90 or resid 91 or resid 92 or resid 93 or resid 94 or resid 95 or resid 96 or resid 97 or resid 98 or resid 99)' #p53 atom selection

sel1 = 'resid 29:30' 
selp53 = 'resid 88:89' 




u1 = u.selectAtoms(sel1); #actual 
print u1;
u2 = u1.CA; 
print u2;    
# selection from p53
dp53 = d.selectAtoms(selp53);
d2 = dp53.CA 
print dp53;
print d2;

for ts in u.trajectory:
    f = MDAnalysis.analysis.distances.dist(u2, d2); 
    print f; 
    
