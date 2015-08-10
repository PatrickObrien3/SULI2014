# One big file for computing contacts and plots for two sets of residues
#Pay attention to sys.argv inputs
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

#files to use for mdmh: junk.pdb  mdmh_MDMX.dcd  mdmh_p53.dcd  MDMX_mdm.pdb  MDMX_p53.pdb

#
#NOTE: u is set to mdma here
#
u = Universe('/home/xov/mdmx/top_dcd/MDMX_mdm.pdb', '/home/xov/mdmx/top_dcd/mdmh_MDMX.dcd');
d = Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd');
ref = Universe('/home/xov/mdmx/top_dcd/junk_both.pdb'); 
print u; 
print d; 
print ref; 



filetitle = sys.argv[1]; # set filetitle to apo/holo and parts being analyzed

"""# ex. 'mdmh_p53_a2'
NOTE: MANUALLY have to change:
        1. residues in sel1
        2. filetitle to accomodate this(in command line)
        3. x - axis on q_matrix plot
        4. x label on q_matrix plot
Old way to load files:        
    u = Universe(sys.argv[1], sys.argv[2]);# set u = mdmx pdb + dcd 
    d = Universe(sys.argv[3], sys.argv[4]); # set d = p53 pdb + dcd 
    ref = Universe(sys.argv[5]);# set ref = junk.pdb

"""

#Sel1 here is the alpha2 helix
tsel1 = 'name CA and (resid 26 or resid 27 or resid 28 or resid 29 or resid 30 or resid 31 or resid 32 or resid 33 or resid 34 or resid 35 or resid 36 or resid 37 or resid 38 or resid 39 or resid 40 or resid 41 or resid 42 or resid 43)' #actual selection used in calculation
tselp53 = 'name CA and (resid 88 or resid 89 or resid 90 or resid 91 or resid 92 or resid 93 or resid 94 or resid 95 or resid 96 or resid 97 or resid 98 or resid 99)' #p53 atom selection

sel1 = 'resid 26:43' #selecting the t2(possibly the most mobile turn of the simulation.
selp53 = 'resid 87:99' 

#selback1 = 'resid 70:73' #backside interact w/p53
#selback2 = 'resid 45-51'#backside interact w/p53

# selections from the mdmx dcd
u1 = u.selectAtoms(sel1); #actual 
print u1;
u2 = u1.CA; 
print u2;    
# selection from p53
dp53 = d.selectAtoms(selp53);
d2 = dp53.CA 
print dp53;
print d2;  
#selections from reference
#print 'the number of atoms from selection 1 is' + u1; 
#print 'the number of atoms from selection p53 is' + dp53; 
refA = ref.selectAtoms(tsel1); 
refB = ref.selectAtoms(tselp53); 
print refA; 
print refB; 



qdata = []
i = 1;     


f = u.trajectory; 

g = d.trajectory;

for ts1, ts2 in itertools.izip(u.trajectory, d.trajectory): 
    Contact = ContactAnalysis1( ref, selection=(tsel1, tselp53), refgroup=(refA, refB), radius=6.0, outfile="%s.dat" % i ); 
    Contact.run(force=False);
    lines = [line.strip().split() for line in open('%s.dat' % i)]
    print lines;
    qdata.append([i, lines[3][1], lines[3][2]]); 
    i += 1;
    print len(qdata);
             
   
    
qa = np.array(qdata); 
#input changed file here, as filename.dat
np.savetxt('q' + str(filetitle) + '.dat', qa, delimiter=" ", fmt="%s"); 

#qplot creates a plot for frame vs. q

def qplot(x, filename=None, **kwargs):
    plotlist = []
    from pylab import plot, xlabel, ylabel, savefig
    kwargs.setdefault('color', 'blue')
    kwargs.setdefault('linewidth', 2)
    x_flt = []
    y_flt = []
    for line in x.readlines():
        l = line.strip().split(); 
        x_flt.append(float(l[0])) 
        y_flt.append(float(l[1])); 
    #print x_flt; 
    #print y_flt;       
    plot(x_flt, y_flt, **kwargs)
    xlabel(r"frame number $t$")
    ylabel(r"native contacts $q_1$")

    if not filename is None:
        savefig(filetitle); 

     
inputfile = open('q' + str(filetitle) + '.dat'); #other ways to work this out with naming if 
print inputfile;                                 # this doesn't work 
qplot(inputfile, filename=('qplot_)' + str(filetitle))); 
#make sure to include second argument for filename

#q_array average

numFiles = 50000
q_initial = np.loadtxt("1.array.gz"); 
qmatrix = q_initial*1; 
for i in range(2, numFiles):
    fname = str(i) + '.array.gz'; 
    f = np.loadtxt(fname); 
    qmatrix = np.add(qmatrix, f); 
    #print qmatrix; 

qavg = qmatrix/numFiles 
np.savetxt('qavg_out', qavg); #can check qavg_out for errors and for 
                              #for redoing the contourf

#qarray plot

def qavg_matrix(c, filename=None, **kwargs):
    
    x = [1, 87];#manually put in residues
    y = [88, 99];    #Can work on automation later
    
    
    kwargs['origin'] = 'lower'
    kwargs.setdefault('aspect', 'equal')
    kwargs.setdefault('interpolation', 'nearest')
    kwargs.setdefault('vmin', 0)
    kwargs.setdefault('vmax', 1)
    kwargs.setdefault('cmap', cm.hot)
    kwargs.setdefault('extent', (min(x), max(x), min(y), max(y))) 
    
    f = contourf(c.T, **kwargs);
    
    xlim(min(x),max(x))
    ylim(min(y),max(y))
    figname=('q avg matrix of' + str(filetitle))
    xlabel("residues 1:87") #change to actual resids
    ylabel("residues 88:99")

    colorbar()

    plot(f);
    #plt.savefig() 
    #plt.show()

    if not filename is None:
            savefig(filename)

qavg_file = np.array(qavg); 
print qavg_file.shape;
qavg_array = np.float_(qavg_file); 
#print qavg_array; 
print qavg_array.shape;   
qavg_matrix(qavg_array, filename=('qmatrix_' + str(filetitle)));
















