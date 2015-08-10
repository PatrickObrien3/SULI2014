#MDAnalysis merge pdb files for every frame
#when print was used to check time, was 200 pdb's per 30seconds
#output is one pdb file for each frame

import MDAnalysis
from MDAnalysis import *
import sys, os
import numpy as np



u = Universe('/home/xov/mdmx/top_dcd/MDMX_mdm.pdb', '/home/xov/mdmx/top_dcd/mdmh_MDMX.dcd'); 
p = Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd');

print u; 
print p; 
i = 50000; 
for ts in u.trajectory[0]:
    usel = u.selectAtoms('protein');
    for ts2 in p.trajectory[0]:
        psel = p.selectAtoms('protein'); 
    merge = MDAnalysis.Merge(usel, psel); 
    merge.atoms.write(str(i) + '.pdb'); 


for i in xrange(1, 50000):
    j = i+1; 
    os.system('mv' + ' ' + str(i) + '.pdb' + ' ' + 'merged_' + str(j) + '.pdb')
    


"""
i = 1; 
for ts in u.trajectory:
    usel = u.selectAtoms('protein');
    for ts2 in p.trajectory[int(i)]:
        psel = p.selectAtoms('protein'); 
    merge = MDAnalysis.Merge(usel, psel); 
    merge.atoms.write(str(i) + '.pdb'); 
    i += 1;
"""     

   

    

    