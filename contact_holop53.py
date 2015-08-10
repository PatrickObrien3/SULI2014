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
u = Universe('/home/xov/mdmx/top_dcd/mdmaww.top', '/home/xov/mdmx/top_dcd/mdma.dcd');
d = Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd');
ref = Universe('/home/xov/mdmx/top_dcd/junk.pdb'); 
print u; 


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


sel1 = 'resid 43:51' #actual selection used in calculation
selp53 = 'resid 88:99' #p53 atom selection
#selback1 = 'resid 70:73' #backside interact w/p53
#selback2 = 'resid 45-51'#backside interact w/p53

# selections from the mdmx dcd
u1 = u.selectAtoms(sel1); print u1;  #actual   
# selection from p53
dp53 = d.selectAtoms(selp53); print dp53; 
#selections from reference
#print 'the number of atoms from selection 1 is' + u1; 
#print 'the number of atoms from selection p53 is' + dp53; 

qdata = []
i = 1;     
for ts1, ts2 in itertools.izip(u.trajectory, d.trajectory):
    if i == 1225:
        print 'not this guy';
    else:
        Contact = ContactAnalysis1( ref, selection=(sel1, selp53), refgroup=(u1, dp53), radius=6.0, outfile="%s.dat" % i ); 
        Contact.run();
        print i; 
        lines = [line.strip().split() for line in open('%s.dat' % i)]
        qdata.append([i, lines[3][1], lines[3][2]]); 
    i += 1;    
   
print 'now generating qa';    
qa = np.array(qdata); 
#input changed file here, as filename.dat
np.savetxt('q' + str(filetitle) + '.dat', qa, delimiter=" ", fmt="%s"); 

#qplot creates a plot for frame vs. q

print 'now making qplot';

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
    if i == 1225:
        print 'not this guy either';
    else:
        fname = str(i) + '.array.gz'; 
        f = np.loadtxt(fname); 
        qmatrix = np.add(qmatrix, f); 
    #print qmatrix; 

qavg = qmatrix/numFiles 
np.savetxt('qavg_out', qavg); #can check qavg_out for errors and for 
                              #for redoing the contourf

#qarray plot

def qavg_matrix(c, filename=None, **kwargs):
    #x = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42];
    #x = [68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80];#manually put in residues
    x = [43, 44, 45, 46, 47, 48, 49, 50, 51];
    y = [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99];    #Can work on automation later
   
    
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
    xlabel("residue from 43:51") #change to actual resids
    ylabel("residue from 88:99")

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
print 'now making qmatrix plot';















