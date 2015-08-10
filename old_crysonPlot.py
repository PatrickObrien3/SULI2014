#Column stack practice; 
"""

author: Patrick O'Brien
date: July 31, 2014

NOTE: Has to be run with ipython/ for some reason python itself isn't working
with matplotlib... keeps running the copy.py script...
"""

import sys, os
import numpy as np
import matplotlib
import matplotlib.pyplot as plt



a1 = []; 
b=1; 
li=[0]; 
for i in xrange(1, 1001):
    x,y=np.loadtxt(str(i)+'00.int', skiprows=1, usecols=(0,1), unpack=True); 
    if b==1:
        li.append(i); 
        #x3.append(float(x)); 
        a1 = np.column_stack((x,y));
        #print a.shape; 
        #print a;  
        b=2; 
    else: 
        a1=np.column_stack((a1,y)); 
        li.append(i); 
        
        #print a.shape; 
        #print a; 
a2=[];
b=1; 
li2=[];
for i in xrange(1, 2001):
    x2,y2=np.loadtxt('/home/xov/mdmx/SANS/mdma/IvsQ/mdma_' + str(i) + '00.int', skiprows=1, usecols=(0,1), unpack=True);
    if b==1:
        li2.append(i);
        a2 = np.column_stack((x2,y2));
        b=2; 
    else:
        a2=np.column_stack((a2,y2)); 
        li2.append(i);    
print len(li); 
print len(a1); 
print 'here is the check'; 
t=np.vstack((li,a1)); 
print t.shape; 
print len(t); 
# len(a1) = 100, t = 101 therefore just put a1+1 for t 
yvalh1 = []
yerrh1 = []; 

for i in xrange(1, (len(a1)+1)): # was len(t); 
    #print i; 
    #print a[int(i)-1,1:]; 
    r = np.average(a1[int(i)-1, 1:]);
    #print r; 
    s = np.std(a1[int(i)-1, 1:]); 
    #print s; 
    yvalh1.append(float(r)); 
    yerrh1.append(float(s));     
 
yvala1=[];
yerra1=[];

for i in xrange(1, len(a1)+1): #was len(t); 
    #print i; 
    #print a[int(i)-1,1:]; 
    r2 = np.average(a2[int(i)-1, 1:]);
    #print r; 
    s2 = np.std(a2[int(i)-1, 1:]); 
    #print s; 
    yvala1.append(float(r2)); 
    yerra1.append(float(s2));
   
#plt.errorbar(x, y, yerr); 
plt.loglog(x, yvalh1); 
plt.errorbar(x, yvalh1, yerrh1, marker='*', linewidth=1.0, color='r', label='MDMX-p53');
plt.loglog(x2,yvala1);
plt.errorbar(x2,yvala1, yerra1, marker='*', linewidth=1.0, color='k', label='MDMX'); 
plt.xlim([0.05, 0.3]); 
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title('I(Q) vs. Q', fontsize=25); 
plt.legend(loc=1); 
plt.show();

#Trying to recreate the Normalized Kratky plots
#Works, but HAS to be normalized due to dependency on I0. 


aI0 = 0.0063744
hI0 = 0.029555


yvalh2= []

for j in xrange(1, len(t)-1): 
    ynew = (((float(x[int(j)])**2)*(float(yvalh1[int(j)])))/(hI0))
    yvalh2.append(float(ynew)); 

print len(yvalh2);

yvala2 = []; 
for j in xrange(1, len(t)-1):
    ynew2 = (((float(x[int(j)])**2)*(float(yvala1[int(j)])))/(hI0))
    yvala2.append(float(ynew2)); 


normYh = []; 
normYa = []; 

yasum = sum(yvala2); 
yhsum = sum(yvalh2); 
for value in yvala2:
    normed = float(value)/yasum; 
    normYa.append(float(normed)); 
print normYa; 
print len(normYa);     

for value in yvalh2:
    normed = float(value)/yasum; 
    normYh.append(float(normed)); 
print 'here is normedYh'; 
print normYh; 
print len(normYh); 

xnew = []; 
for j in xrange(1, len(t)-1):
    xnew.append(x[int(j)]); 

print 'length of xnew'; 
print len(xnew); 


#Kratky Plot                      
                                   
plt.plot(xnew, normYh, color='r', marker='*', label='MDMX-p53');
plt.plot(xnew, normYa, color='k', marker='*', label='MDMX'); 
plt.legend(loc=1);  
plt.show();   


 
 
 
     
       
          
                
"""    
print 'here is lenq and q'; 
print len(q); 
print q; 


print 'avg= way'; 
avg = np.average(a, axis=1); 
print avg.shape; 
print avg; 
"""

print 'done'; 
