#Use contourf
import MDAnalysis
import numpy as np
import sys, os 
from MDAnalysis import * 
from MDAnalysis.analysis import *
from MDAnalysis.analysis.contacts import *
from MDAnalysis.analysis.distances import *
import pylab
import numpy.linalg
import matplotlib
import matplotlib.pyplot as plt

def qavg_matrix(c, filename=None, **kwargs):
    from matplotlib.pyplot import *
    x = [1, 87]; #turn3a4
    y = [1, 87]; #p53
    
    
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
    figname=(sys.argv[2])
    xlabel("residue from 1:87")#
    ylabel("residue from 1:87")#

    colorbar()

    plot(f);
    #plt.savefig() 
    #plt.show()

    if not filename is None:
            savefig(filename)

qavg_file = np.loadtxt(sys.argv[1]); 
print qavg_file.shape;
qavg_array = np.float_(qavg_file); 
print qavg_array; 
print qavg_array.shape;   
qavg_matrix(qavg_array, filename=(sys.argv[2]));
