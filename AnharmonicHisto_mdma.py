import numpy   #import numpy
import math    # import math
import scipy.stats #import scipy.stats

from KabschAlign import * #methods for calc. roation matrix that minimizes RMSD JPO
from IterativeMeansAlign import * #ask. resolves multiple alignment of pairwise alignments? JPO

from MDAnalysis import *

from jade import *

u = MDAnalysis.Universe('/home/xov/mdmx/top_dcd/mdmaww.top', '/home/xov/mdmx/top_dcd/mdma.dcd', permissive=False);
#u = MDAnalysis.Universe('../../tmp/2V93_1.pdb', '../../tmp/2V93.dcd', permissive=False);
ca = u.selectAtoms('name CA');
#ca = u.selectAtoms('not (type H)');
cacoords = []; frames = []; 

for ts in u.trajectory:     #iterate through all frames
	f = ca.coordinates();  
	cacoords.append(f.T);   #appends transposed coordinates of CA to cacoords list
	frames.append(ts.frame);  #appends corresponding frame to the frames list
print len(cacoords); 
print numpy.shape(cacoords);

dim = 3; Na = 87; #need to change Na to the right number of atoms selected

iterAlign = IterativeMeansAlign();
[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(cacoords, 0.001, 5);# maxitr changed to 5 from 20 from 4
#perform the iterativemeansalign

print numpy.shape(eRMSD);

coords = numpy.reshape(newCoords, (len(newCoords), dim*Na)).T; 
print 'coords: ', numpy.shape(coords); 
avgCoords = numpy.mean(coords, 1); print avgCoords;
print 'avgCoords: ', numpy.shape(avgCoords);
tmp = numpy.reshape(numpy.tile(avgCoords, 100000), (100000,dim*Na)).T; #changed 50000 to 100000
caDevsMD = coords - tmp;                                             #for frame number I think
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
plt.savefig(filename='mdma_QAA_fig1');
plt.show();


print 'Mean: ', gm;
print 'Std. dev: ', gs;
print 'Kurtosis: ', gK;

cc = coords[:,0]; print numpy.shape(cc);
cc = numpy.reshape(cc, (dim,Na));
#print numpy.shape(coords[0:-1:3,0]), numpy.shape(coords[1:-1:3,0]), numpy.shape(coords[2:-1:3,0]);

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
ax.plot(cc[0,:], cc[1,:], cc[2,:]);
plt.savefig(filename='mdma_QAA_fig2');
plt.show();

print numpy.shape(numpy.cov(coords));
[pcas,pcab] = numpy.linalg.eig(numpy.cov(coords));
si = numpy.argsort(-pcas.ravel()); print si;
pcaTmp = pcas;
pcas = numpy.diag(pcas);
pcab = pcab[:,si];

print 'pcas is '; 
#print pcas; 

print 'pcab is';
#print pcab; 

print 'si is '; 
#print si; 

#fig = plt.figure();
#ax = fig.add_subplot(111);
#cs = ax.contourf(numpy.cov(coords));
#ax.colorbar(cs); 
#plt.show();

fig = plt.figure();
ax = fig.add_subplot(111);
y = numpy.cumsum(pcaTmp.ravel()/numpy.sum(pcaTmp.ravel()));
ax.plot(y);
plt.savefig(filename='mdma_QAA_fig3');
plt.show();

fig = plt.figure();
ax = fig.add_subplot(111, projection='3d');
pcacoffs = numpy.dot(pcab.conj().T, caDevsMD);
print numpy.shape(pcacoffs);
ax.scatter(pcacoffs[0,:], pcacoffs[1,:], pcacoffs[2,:], marker='o', c=[0.6,0.6,0.6]);
plt.savefig(filename='mdma_QAA_fig4');
plt.show();

# some set up for running JADE
Ncyc  = 1;
subspace = 50; #50 covers ~95 percent of variance. 
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
plt.savefig(filename='mdma_QAA_fig5');
plt.show();