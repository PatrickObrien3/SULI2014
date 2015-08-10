"""
Author: James Pino
Adapted for MDMX by Patrick O'Brien
for chi-squared analysis here;

input is the cryson_summary.txt file produced after a Cryson run.
"""
import sys, os
import numpy as np


a=1
#f=open('chiSquared_mdmh.txt','w')

chih= []; 
for line in open("cryson_summary.txt"):
	if "Rg" in line:  
		#print>>f, a, line[-8:]
		a=a+1
		chih.append(float(line[-8:]))
  
#method 2; 
 
chisq = []; 
for i in xrange(1, (len(chih))):
    chisq.append(float((chih[int(i)])**2))
#print hsq[1];

#avg2 = float(sumhsq/len(hsq));
avg = np.average(chisq);   
std = np.std(hsq); 
print 'The chi-squared is %s and the standard deviation is %s' %(avg, std); 





