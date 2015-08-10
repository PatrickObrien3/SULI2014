#creates a plot for frame vs. q

import MDAnalysis
import numpy as np
import sys, os 
from MDAnalysis import * 
from MDAnalysis.analysis import *
from MDAnalysis.analysis.contacts import *
from MDAnalysis.analysis.distances import *
import pylab

def plottest(x, filename=None, **kwargs):
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
    print x_flt; 
    print y_flt;       
    plot(x_flt, y_flt, **kwargs)
    xlabel(r"frame number $t$")
    ylabel(r"native contacts $q_1$")

    if not filename is None:
        savefig(filename); 
    
inputfile = open(sys.argv[1]);
print inputfile; 
plottest(inputfile, filename=(sys.argv[2])); 
#make sure to include second argument for filename





"""
f = ContactAnalysis1.timeseries((sys.argv[1]));
C = ContactAnalysis1.load(f);
C.plot(filename=C, linewidth=1, color="blue");

"""

"""for line in x.readlines():
        a = line.strip().split(); 
        plotlist.append(a);
    print plotlist;
    for line in x.readlines():
        f = line.split()
        x_str.append((f[0]))
        y_str.append((f[1]))
    x_flt = [float(i) for i in x[0]];
    y_flt = [float(j) for j in x[1]];
    print x_str; 
    print y_str;
    for line in x_str:
        x_flt.append(int(line([0])));
    print x_flt"""