#dihedral2 degrees with no Iterativemeansalign.

#Runs all the way through; still needs some fine tuning though. 
import sys, os
import MDAnalysis
from MDAnalysis import *
from MDAnalysis.core import *
import numpy as np
import math as m
import scipy.stats
from IterativeMeansAlign_dQAA_p53 import *
from KabschAlign_p53 import *
from jade import *


u = Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd'); 


protein = u.selectAtoms('protein'); 
Na = protein.numberOfResidues(); 
print Na;

tmplist = [];
dicoords = [];
frames = [];

dim = 4;

for ts in u.trajectory[0:500]:
    frames.append(ts.frame);
    for res in range(2, Na-1):# need numresidues -1? Answer: Yes; otherwise not enough Atoms for final calc.
        #print "Processing residue %d" % res
        phi_sel = u.residues[res].phi_selection(); 
        phi_dih = phi_sel.dihedral(); #in degrees
        
        psi_sel = u.residues[res].psi_selection(); 
        psi_dih = psi_sel.dihedral(); #in degrees
        
        xr = m.radians(phi_dih); x = m.cos(xr); #xd = m.degrees(x);  
        yr = m.radians(phi_dih); y = m.sin(yr); #yd = m.degrees(y); 
        zr = m.radians(psi_dih); z = m.cos(zr); #zd = m.degrees(z); 
        wr = m.radians(psi_dih); w = m.sin(wr); #wd = m.degrees(w); 
        #print x; print y; print z; print w; 
    
        tmplist.append([x, y, z, w]);
        #print f.shape; 
          
    
    f = np.array(tmplist); 
    #print f.shape
    dicoords.append(f.T);
    tmplist=[];
print len(dicoords); 
print np.shape(dicoords);
  
#print newlist;  
#print tmplist;


NaN= Na-3; # the number of calculated phi/psi angles. equal to Na - 3
           # due to there only being phi/psi after/before the termini
print NaN; 

#iterAlign = IterativeMeansAlign_dQAA_p53();
#[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(dicoords, 0.005, 30360);# maxitr changed to 5 from 4
#perform the iterativemeansalign

#print numpy.shape(eRMSD);

coords = numpy.reshape(dicoords, (len(dicoords), dim*NaN)).T; #NaN specified above.  
print 'coords: ', numpy.shape(coords); 
avgCoords = numpy.mean(coords, 1); print avgCoords;
print 'avgCoords: ', numpy.shape(avgCoords);
tmp = numpy.reshape(numpy.tile(avgCoords, 500), (500,dim*NaN)).T; 
caDevsMD = coords - tmp;                                             
#print numpy.shape(caDevsMD); print caDevsMD[0];

D = caDevsMD.flatten(); print numpy.shape(D);
gm = numpy.mean(D); #Mean
gs = numpy.std(D); #std. Dev
gK = scipy.stats.kurtosis(D,0,fisher=False); #kurtosis

[n,s] = numpy.histogram(D, bins=51,normed=1);

gp = numpy.exp(-(s-gm)**2/(2*gs*gs));
gp = gp/numpy.sum(gp); print 'gp is:', numpy.shape(gp);

lo = 0; hi = len(s);
print 'check 1, 2, 3'; 
fig = plt.figure();
ax = fig.add_subplot(111);
x = 0.5*(s[1:] + s[:-1]);
#ax.semilogy(s[lo:hi], gp[lo:hi],'c-',linewidth=2);
ax.hold(True); 
ax.semilogy(x, n, 'k-', linewidth=2.0); ax.axis('tight');
#plt.savefig(filename='rad53_fig1');
plt.show();


print 'Mean: ', gm;
print 'Std. dev: ', gs;
print 'Kurtosis: ', gK;

cc = coords[:,0]; print numpy.shape(cc);
cc = numpy.reshape(cc, (dim,NaN));
#print numpy.shape(coords[0:-1:3,0]), numpy.shape(coords[1:-1:3,0]), numpy.shape(coords[2:-1:3,0]);

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
ax.plot(cc[0,:], cc[1,:], cc[2,:]);
#plt.savefig(filename='radp53_fig2');
plt.show();





print numpy.shape(numpy.cov(coords));
[pcas,pcab] = numpy.linalg.eig(numpy.cov(coords)); #[values,vectors]?
si = numpy.argsort(-pcas.ravel()); print si; np.savetxt('siTest', si);
pcaTmp = pcas;
pcas = numpy.diag(pcas);
pcab = pcab[:,si];

print pcas.shape;
 
print pcas; 
np.savetxt('pcasTest', pcas)
print 'next'
print pcab.shape
print pcab;
np.savetxt('pcabTest', pcab);  

#fig = plt.figure();
#ax = fig.add_subplot(111);
#cs = ax.contourf(numpy.cov(coords));
#ax.colorbar(cs); 
#plt.show();

fig = plt.figure();
ax = fig.add_subplot(111);
y = numpy.cumsum(pcaTmp.ravel()/numpy.sum(pcaTmp.ravel()));
ax.plot(y);
#plt.savefig(filename='radp53_fig3');
plt.show();

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
pcacoffs = numpy.dot(pcab.conj().T, caDevsMD);
print numpy.shape(pcacoffs);
ax.scatter(pcacoffs[0,:], pcacoffs[1,:], pcacoffs[2,:], marker='o', c=[0.6,0.6,0.6]);
#plt.savefig(filename='radp53_fig4');
plt.show();

# some set up for running JADE
Ncyc  = 1;
subspace = 20; #20 covers ~95 percent variance. 
lastEig = subspace; # number of eigen-modes to be considered
numOfIC = subspace; # number of independent components to be resolved

icajade = jadeR(coords, lastEig); 
print numpy.shape(icajade);
icacoffs = numpy.dot(icajade, caDevsMD);
icacoffs = numpy.asarray(icacoffs); 
print 'icacoffs: ', numpy.shape(icacoffs);

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
ax.scatter(icacoffs[0,:], icacoffs[1,:], icacoffs[2,:], marker='o', c=[0.6,0.6,0.6]); 
#plt.savefig(filename='radp53_fig5');
plt.show();




"""
print 'here is 0'
print dicoords[0];
print 'here is 1';  
print dicoords[1];
print 'here is 2'; 
print dicoords[2];

"""