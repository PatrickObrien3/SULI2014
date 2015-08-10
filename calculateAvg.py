import os, string, sys
import numpy 
import matplotlib
import matplotlib.pyplot as plt



#flist = ['p27d2.16.out', 'p27d2.19.out', 'p27d2.27.out', 'p27d2.29.out', 'p27d2.33.out', 'p27d2.35.out', 'p27d2.885.out', 'p27d2.886.out', 'p27d2.887.out', 'p27d2.889.out', 'p27d2.891.out','p27d2.896.out'];

CAshift = []; 
CBshift = [];

numFiles = 10;
resList = [];
j = 0
for i in range(1,numFiles,):
	fname = 'mdma_' + str(i) + '.out';
	f = open(fname, 'r');
	for line in f.readlines():
		l = line.strip().split();
		if len(l) == 0:
			break;
		if l[0] == '---' or l[0] == 'NUM':
			print line;
		elif i == 1:
			x = '';
			if l[0][0] == '*':
				x = l[0][1:-1];
			else:
				x = l[0];
			resList.append(l[1] + x);
		else:
			CAshift.append(float(l[5]));
			CBshift.append(float(l[6]));
		#print len(CAshift);
	i = i + 1;
	f.close();
print len(CAshift) 
CAshift = numpy.reshape(CAshift, (87,numFiles-2));# first int from len(CAshift)/(numFiles-2)
CBshift = numpy.reshape(CBshift, (87,numFiles-2));

avgChemCAShift = numpy.mean(CAshift,axis=1);
avgChemCBShift = numpy.mean(CBshift,axis=1); 
stdChemCAShift = numpy.std(CAshift,axis=1);
stdChemCBShift = numpy.std(CBshift,axis=1);
"""
f = open('avgChemShifts.dat','w');
print >> f, '%6s%10s%10s%10s%10s' %('resID','meanCA', 'stdCA', 'meanCB', 'stdCB');
for x in range(0, 87): #Need to change to 87? 
	print >> f, '%10s%8.3f%8.3f%8.3f%8.3f' %(resList[x], avgChemCAShift[x], stdChemCAShift[x], avgChemCBShift[x], stdChemCBShift[x]);
f.close();
"""
print avgChemCAShift; 
print avgChemCAShift.shape; 
print stdChemCAShift.shape;
x = numpy.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87])
print x.shape;
y = avgChemCAShift;
e = stdChemCAShift; 
"""
plt.errorbar(x, y, e, linestyle='None', markersize=10, marker='*')
plt.ylim((52, 63))
plt.savefig(filename='test_mdma_cshift' + '.pdf'); 
plt.show();
"""


