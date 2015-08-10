"""
Script to find average of RG and standard deviation of RG from summary file
produced by cryson

Created by Patrick O'Brien

Part 1: Gets RG values from the cryson_summary report(created by James Pino)
Part 2: calculates average and std from those numbers. 

Utilized a script to initially sort the frame number and RG value into a separate file
that will be the input

"""

import os, sys
import numpy as np

import math 

a=1
h=open('out.txt','w')
for line in open("cryson_summary_mdma.txt"):
	if "Rg" in line:
		#print a, line[-8:]
		print>>h, a, line[-8:]
		a=a+1

RG = []; frame = []; 
f = open('out.txt'); 
w = open('avg_std.out', 'w'); 
print f; 
i = 1; 
for line in f.readlines(): 
    l = line.strip().split();
    if len(l) == 0 or len(l) == 1:
        print 'skip';
        i +=1      
    else:
        print str(i); 
        print l; 
        print float(l[0]); 
        print float(l[1]);   
        RG.append(float(l[1])); 
        frame.append(float(l[0]));
        i += 1 
print len(RG); 
print len(frame); 

mean = np.mean(RG); 
RG2 = np.array(RG);
print RG2.shape;  
mean2 = np.mean(RG2);
 
print mean
std = np.std(RG); 
print std; 
print>>w, 'mean   std'; 
print>>w, mean, std  


    