
import sys, os
import numpy
import matplotlib
from matplotlib import *
import matplotlib.pyplot as plt

f = open(sys.argv[1]); #set as mdmh avgcshift.dat
g = open(sys.argv[2]); #set as mdma avgcshift.dat



mdmh_avgChemCAShift = [];
mdmh_stdChemCAShift = []; 

mdma_avgChemCAShift = [];
mdma_stdChemCAShift = []; 



for line in f.readlines():
    l = line.strip().split()
    mdmh_avgChemCAShift.append(float(l[1]));
    mdmh_stdChemCAShift.append(float(l[2]));
    
for line in g.readlines():
    l = line.strip().split()
    mdma_avgChemCAShift.append(float(l[1])); 
    mdma_stdChemCAShift.append(float(l[2]));

"""
mdmh_avgChemCAShift.remove('meanCA') 
mdmh_stdChemCAShift.remove('stdCA')  

mdma_avgChemCAShift.remove('meanCA') 
mdma_stdChemCAShift.remove('stdCA')
"""





mdmh_avgcshift = numpy.array((mdmh_avgChemCAShift));    
mdmh_stdcshift = numpy.array((mdmh_stdChemCAShift));            
             
mdma_avgcshift = numpy.array(mdma_avgChemCAShift);
mdma_stdcshift = numpy.array(mdma_stdChemCAShift);



print mdmh_avgcshift; 
print mdmh_stdcshift.shape;
print mdma_avgcshift.shape; 
print mdma_stdcshift.shape;
x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87])
print x.shape;
y = mdmh_avgcshift;
e = mdmh_stdcshift;
plt.errorbar(x, y, e, linestyle='None', markersize=5, marker='*', label='mdmh')

y = mdma_avgcshift;
e = mdma_stdcshift;
plt.errorbar(x, y, e, linestyle='None', markersize=5, marker='*', color='r', label='mdma')
plt.ylim((52, 62))
plt.legend()
plt.savefig(filename='mdmx_cshift_eb' + '.pdf'); 
plt.show();


y = mdmh_avgcshift;
e = mdmh_stdcshift;
plt.plot(x, y, linestyle='None', markersize=5, marker='*', label='mdmh')


y = mdma_avgcshift;
e = mdma_stdcshift;
plt.plot(x, y, linestyle='None', markersize=5, marker='*', color='r', label='mdma')
plt.ylim((56, 58))
plt.legend()
plt.savefig(filename='mdmx_cshift' + '.pdf'); 
plt.show();






