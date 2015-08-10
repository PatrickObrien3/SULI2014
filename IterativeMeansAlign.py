import MDAnalysis
import numpy
import numpy.linalg
import math
from KabschAlign import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

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
			#print mnC;
			#print mnC.shape;  
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
	u = MDAnalysis.Universe('/home/xov/pyaca/data/ubq_1111.pdb', '/home/xov/pyaca/data/UBQ_500ns.dcd', permissive=False);
	ca = u.selectAtoms('name CA');
	cacoords = []; frames = [];
	for ts in u.trajectory[0:10000:5]:
		f = ca.coordinates();
		cacoords.append(f.T);
		frames.append(ts.frame);
	print numpy.shape(cacoords);
	print frames;
	iterAlign = IterativeMeansAlign();
	[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(cacoords, 0.001, 4); 
	
	print numpy.shape(eRMSD);
	newCoords = numpy.array(newCoords);
	newCoords = numpy.reshape(newCoords, (2000,3*69)); print numpy.shape(newCoords); 
	fig = plt.figure();
	ax = fig.add_subplot(111);
	ax.plot(frames, eRMSD[1], linestyle='solid', linewidth=2.0);
	plt.show();

