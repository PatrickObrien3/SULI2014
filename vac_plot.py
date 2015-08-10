#autocorrelation plot

import numpy
import matplotlib
import matplotlib.pyplot as plt
import sys, os


inputFile = open(sys.argv[1]); 

frame = []
vac = []


for line in inputFile:
    f = line.strip().split()
    #print f;
    if f[0] == '#Frame':
        print 'skip';
    else:
        frame.append(float(f[0]));
        vac.append(float(f[1]));

print len(frame); 
print len(vac);
avg = numpy.mean(vac); 
print avg; 
#print vac; 



plt.plot(frame, vac)
plt.ylim(-.002, 0.004)
plt.xlim(0, 260); 
plt.show();  
 
    