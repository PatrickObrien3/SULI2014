 #contact apo 
import MDAnalysis
import numpy as np
import sys, os 
from MDAnalysis import * 
from MDAnalysis.analysis import *
from MDAnalysis.analysis.contacts import *


#
#                            Use this contact file for MDMA contact
#                            analysis. Much easier than the mdmh analysis
#                            script
#


u = Universe('/home/xov/mdmx/top_dcd/mdmaww.top', '/home/xov/mdmx/top_dcd/mdma.dcd');
filetitle = (sys.argv[1]); #make sure identifiable, i.e. "mdma_44-49_27-40"
 
#Designate selections underneath this line:
#sel1 = the mdma alpha 2 helix
#sel2 = the turn3 and alpha 4 helix 
#these together form much of the binding pocket
sel1 = 'resid 26:42' #t2
sel2 = 'resid 68:82' #B3
ref1 = u.selectAtoms(sel1); 
ref2 = u.selectAtoms(sel2); 

print ref1; 
print ref2; 



C12 = ContactAnalysis1( u, selection=(sel1, sel2), refgroup=(ref1, ref2), radius=6.0, outfile=(str(filetitle) + ".dat")); 
C12.run(); 

C12.plot(filename=(str(filetitle)), linewidth=1, color="green"); 
#C12.plot_qavg(filename=('qmatrix_' + str(filetitle) + '.pdf')); 


#
#          Here is a list of sample selections from MDMA found on vmd 
#
#

"""
selB1 = 'resid 1:9'; #beginning, not important
selA1 = 'resid 9:20';#alpha helix 1
selT1 = 'resid 20:26'; #turn 1
selA2 = 'resid 27:40'; #alpha helix 2
selT2 = 'resid 42:51'; #turn 2, biggest mover!
selB2 = 'resid 51:57'; #Beta sheet two
selA3 = 'resid 58:64'; #alpha helix three
selB3 = 'resid 65:70'; #Beta sheet connecting to Beta 2, PHE68; 
selA4 = 'resid 71:80'; # alpha helix 4
selB4 = 'resid 81:87';
selp53 = 'resid 88:99'
selback = 'resid 70:73'
selback2 = 'resid 45-51'
"""

