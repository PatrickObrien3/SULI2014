"""
script to write out all the CA coordinates

Author Patrick O'Brien
date: 8/4/14
"""

import MDAnalysis
from MDAnalysis import *
import numpy as np

#U = Universe('/home/xov/mdmx/top_dcd/mdmaww.top', '/home/xov/mdmx/top_dcd/mdma.dcd'); #apo
U = Universe('/home/xov/mdmx/top_dcd/MDMX_mdm.pdb', '/home/xov/mdmx/top_dcd/mdmh_MDMX.dcd'); #holo


CA = U.selectAtoms("name CA"); 
W = MDAnalysis.Writer("mdmh_CA.pdb", multiframe=True); 
for ts in U.trajectory:
    W.write(CA); 
W.close(); 


