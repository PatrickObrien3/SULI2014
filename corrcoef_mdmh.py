#covariance coefficients of mdmh and p53 

import sys, os
import MDAnalysis
import numpy
import numpy.linalg
import math
from KabschAlign import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

def qavg_matrix(c, filename=None, **kwargs):
    from matplotlib.pyplot import *
    x = [26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42]; #
    y = [88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99]; #p53
    
    
    kwargs['origin'] = 'lower'
    kwargs.setdefault('aspect', 'equal')
    kwargs.setdefault('interpolation', 'nearest')
    kwargs.setdefault('vmin=', 0)
    kwargs.setdefault('vmax=', 1.000)
    kwargs.setdefault('cmap', cm.hot)
    kwargs.setdefault('extent', (min(x), max(x), min(y), max(y)))
    
    
    f = contourf(c, **kwargs);
    
    xlim(min(x),max(x))
    ylim(min(y),max(y))
    figname=(sys.argv[1])
    xlabel("residue from 26:42")#
    ylabel("residue from 88:99") #p53

    colorbar()

    plot(f);
    #plt.savefig() 
    #$plt.show()

    if not filename is None:
            savefig(filename)










class IterativeMeansAlign(object):
	
	def __init__(self):
		"""
		Constructor
		"""

	def iterativeMeans(self, coords, eps, maxIter):
		# all coordinates are expected to be passed as a (Ns x 3 x Na)  array
		# where Na = number of atoms; Ns = number of snapshots
		Ns = numpy.shape(coords)[0]; print Ns; 
		dim = numpy.shape(coords)[1]; print dim;
		Na = numpy.shape(coords)[2]; print Na;
		
		avgCoords = [];			# track average coordinates
		kalign = KabschAlign();		# initialize for use

		ok = 0;				# tracking convergence of iterative means
		itr = 1; 			# iteration number
		
		eRMSD = [];
		
		while not(ok):
			tmpRMSD = [];
			mnC = numpy.mean(coords, 0); 
			avgCoords.append(mnC);
			for i in range(0,Ns):
				fromXYZ = coords[i]; 	
				[R, T, xRMSD, err] = kalign.kabsch(mnC, fromXYZ);
				#print T;
				tmpRMSD.append(xRMSD); 
				tmp = numpy.reshape(numpy.tile(T, Na), (Na, dim)).T;
				pxyz = numpy.dot(R,fromXYZ) + tmp;  
				coords[i] = pxyz;
			eRMSD.append(numpy.array(tmpRMSD).T);
			newMnC = numpy.mean(coords,0); 
			err = math.sqrt(sum((mnC.flatten()-newMnC.flatten())**2))
			print itr, err
			if err <= eps or itr == maxIter:
				ok = 1;
			itr = itr + 1;
		return [itr,avgCoords,eRMSD,coords];

if __name__=='__main__':
	u = MDAnalysis.Universe('/home/xov/MDMX/7114/MDMX_mdm.pdb', '/home/xov/MDMX/mdmh_MDMX.dcd', permissive=False);
	uselections = u.selectAtoms('name CA and (resid 26 or resid 27 or resid 28 or resid 29 or resid 30 or resid 31 or resid 32 or resid 33 or resid 34 or resid 35 or resid 36 or resid 37 or resid 38 or resid 39 or resid 40 or resid 41 or resid 42)'); 
	# u = turn 2(moving turn)
	print 'mdmh selections  '; 
	print uselections;
	cacoords = []; frames = [];
	for ts in u.trajectory[0:50000]:
		f = uselections.coordinates();
		cacoords.append(f.T);
		frames.append(ts.frame);
	print numpy.shape(cacoords);
	#print cacoords; 
	#print frames;
	iterAlign = IterativeMeansAlign();
	[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(cacoords, 0.001, 4); 
	
	print eRMSD;
	print numpy.shape(eRMSD);
	
	mdmh_rmsd = numpy.array(eRMSD);
	"""
	print 'here is shape of mdmh_rmsd:';
	print numpy.shape(mdmh_rmsd);
	
	A = numpy.cov(mdmh_rmsd); 
	
	print numpy.shape(A); 
	print A; 
	print 'here is B:' 

	B = numpy.corrcoef(mdmh_rmsd.T); 
	print numpy.shape(B); 
	print B;
	""" 

class IterativeMeansAlign2(object):
	
	def __init__(self):
		"""
		Constructor
		"""

	def iterativeMeans2(self, coords, eps, maxIter):
		# all coordinates are expected to be passed as a (Ns x 3 x Na)  array
		# where Na = number of atoms; Ns = number of snapshots
		Ns = numpy.shape(coords)[0]; print Ns; 
		dim = numpy.shape(coords)[1]; print dim;
		Na = numpy.shape(coords)[2]; print Na;
		
		avgCoords = [];			# track average coordinates
		kalign = KabschAlign();		# initialize for use

		ok = 0;				# tracking convergence of iterative means
		itr = 1; 			# iteration number
		
		eRMSD2 = [];
		
		while not(ok):
			tmpRMSD = [];
			mnC = numpy.mean(coords, 0); 
			avgCoords.append(mnC);
			for i in range(0,Ns):
				fromXYZ = coords[i]; 	
				[R, T, xRMSD, err] = kalign.kabsch(mnC, fromXYZ);
				#print T;
				tmpRMSD.append(xRMSD); 
				tmp = numpy.reshape(numpy.tile(T, Na), (Na, dim)).T;
				pxyz = numpy.dot(R,fromXYZ) + tmp;  
				coords[i] = pxyz;
			eRMSD2.append(numpy.array(tmpRMSD).T);
			newMnC = numpy.mean(coords,0); 
			err = math.sqrt(sum((mnC.flatten()-newMnC.flatten())**2))
			print itr, err
			if err <= eps or itr == maxIter:
				ok = 1;
			itr = itr + 1;
		return [itr,avgCoords,eRMSD2,coords];

if __name__=='__main__':
	
	p53 = MDAnalysis.Universe('/home/xov/MDMX/MDMX_p53.pdb', '/home/xov/MDMX/mdmh_p53.dcd', permissive=False)
	p53selections = p53.selectAtoms('name CA and (resid 88 or resid 89 or resid 90 or resid 91 or resid 92 or resid 93 or resid 94 or resid 95 or resid 96 or resid 97 or resid 98 or resid 99)')
	print 'p534 selection  ';
	print p53selections; 
	cacoords = []; frames = [];
	for ts in p53.trajectory[0:50000]:
		g = p53selections.coordinates();
		cacoords.append(g.T);
		frames.append(ts.frame);
	print numpy.shape(cacoords)
	#print cacoords; 
	#print frames;
	iterAlign = IterativeMeansAlign2();
	[itr, avgCoords, eRMSD2, newCoords] = iterAlign.iterativeMeans2(cacoords, 0.001, 4); 
	
	print eRMSD2;
	print numpy.shape(eRMSD2);
	
	p53_rmsd = numpy.array(eRMSD2);
	"""
	print 'here is shape of p53_rmsd:';
	print numpy.shape(p53_rmsd);
	
	A = numpy.cov(p53_rmsd); 
	
	print numpy.shape(A); 
	print A; 
	print 'here is B:' 

	B = numpy.corrcoef(p53_rmsd.T); 
	print numpy.shape(B); 
	print B;
	"""
		
Both_cov = numpy.cov(mdmh_rmsd, p53_rmsd); 
print numpy.shape(Both_cov); 
print Both_cov; 

Both_corrcoef = numpy.corrcoef(mdmh_rmsd, p53_rmsd); 

print numpy.shape(Both_corrcoef);
print Both_corrcoef;

 

qavg_matrix(Both_corrcoef, filename=(sys.argv[1]));

		
	