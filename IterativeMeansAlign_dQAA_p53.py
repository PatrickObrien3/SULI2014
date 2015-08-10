#dQAA for p53


import MDAnalysis
import numpy
import numpy.linalg
import math
from KabschAlign_p53 import *

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

class IterativeMeansAlign_dQAA_p53(object):
	
	def __init__(self):
		"""
		Constructor
		"""

	def iterativeMeans(self, coords, eps, maxIter):
		# all coordinates are expected to be passed as a (Ns x 3 x Na)  array
		# where Na = number of atoms; Ns = number of snapshots
		Ns = numpy.shape(coords)[0]; print Ns; 
		#Ns = 100; print Ns; 
		dim = numpy.shape(coords)[1]; print dim;
		#Na = 12;print Na;
		Na = numpy.shape(coords)[2]; print Na;
		
		avgCoords = [];			# track average coordinates
		kalign = KabschAlign_p53();		# initialize for use

		ok = 0;				# tracking convergence of iterative means
		itr = 1; 			# iteration number
		
		eRMSD = [];
		
		while not(ok):
			tmpRMSD = [];
			mnC = numpy.mean(coords, 0);
			#print mnC 
			print mnC.shape
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
	u = MDAnalysis.Universe('/home/xov/mdmx/top_dcd/MDMX_p53.pdb', '/home/xov/mdmx/top_dcd/mdmh_p53.dcd', permissive=False);
	#u = MDAnalysis.Universe('/home/xov/pyaca/data/ubq_1111.pdb', '/home/xov/pyaca/data/UBQ_500ns.dcd', permissive=False);
	ca = u.selectAtoms('name CA');
	cacoords = []; frames = [];
	dicoords = []; tmplist = []; 
	
	for ts in u.trajectory[0:50000:500]:
		frames.append(ts.frame);
                for res in range(2, Na-1):# need numresidues -1? Answer: Yes; otherwise not enough Atoms for final calc.
                #print "Processing residue %d" % res
                    phi_sel = u.residues[res].phi_selection(); 
                    phi_dih = phi_sel.dihedral(); #in degrees
        
                    psi_sel = u.residues[res].psi_selection(); 
                    psi_dih = psi_sel.dihedral(); #in degrees
        
                    xr = m.radians(phi_dih); x = m.cos(xr); #convert to radians before 
                    yr = m.radians(phi_dih); y = m.sin(yr); #cos/sin function
                    zr = m.radians(psi_dih); z = m.cos(zr); 
                    wr = m.radians(psi_dih); w = m.sin(wr); 
                    #print x; print y; print z; print w; 
    
                    tmplist.append([x, y, z, w]);
                    #print f.shape;;
	f = numpy.array(tmplist); 
	print f.shape; 
	dicoords.append(f.T); 
	
	print numpy.shape(cacoords);
	
	#print frames;
	
	iterAlign = IterativeMeansAlign();
	[itr, avgCoords, eRMSD, newCoords] = iterAlign.iterativeMeans(dicoords, 0.001, 4); 
	
	print numpy.shape(eRMSD);
	newCoords = numpy.array(newCoords);
	newCoords = numpy.reshape(newCoords, (2000,3*69)); print numpy.shape(newCoords); 
	fig = plt.figure();
	ax = fig.add_subplot(111);
	ax.plot(frames, eRMSD[1], linestyle='solid', linewidth=2.0);
	plt.show();

