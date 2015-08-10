"""

Cryson command plus analysis to experimental data; 

author: Patrick O'Brien
date: 8/5/14

Cryson input to run was: 
 cryson 9.pdb /home/xov/mdmx/SANS/Exp/MX53.dat /res 
 /home/xov/atsas/atsas-2.5.2-1/share/doc/atsas-2.5.2/cryson/example/ill.res 
 -sm 0.51 -ns 100 -dro 0.0 -err
all in one line. if the line doesn't extend as far on the x axis as far as it needs to
you might need to extend the -sm value. Refer to CRYSON and CRYSOL manuals from ATSAS 
for further reference.     
    
Datetime was used to start a run at a certain time    
    
"""

import sys, os
import numpy as np
import matplotlib 
import matplotlib.pyplot as plt
import datetime as dt
import time
"""
t1 = dt.time(10, 0, 0); 
print t1; 


while True:
    if dt.datetime.now().hour in range(6, 11):
        print 'sleep time';
        time.sleep(60)
        
    else:
        time.sleep(10)
"""
#os.system(" cryson "+ "'mdma_*.pdb'"+" /home/xov/mdmx/SANS/Exp/MDA.dat /res /home/xov/atsas/atsas-2.5.2-1/share/doc/atsas-2.5.2/cryson/example/ill.res -sm 0.51 -ns 100 -dro 0.0 -err");     
#os.system("mkdir mdmaFit"); 
#os.system("mv" + " *.fit" + " mdmaFit"); 




# Prepare the Experimental parts of the graphs; 
# requires only the experimental txt/dat files
apo = open('/home/xov/mdmx/SANS/Exp/MDA.dat'); #apo
holo = open('/home/xov/mdmx/SANS/Exp/MX53.dat'); #holo

exax = []; exay = []; exaerr = []; exhx = []; exhy = []; exherr = []; 

for line in apo.readlines():
    if line.startswith('#'):
        print "skip"
    else:
        l = line.strip(',').split(','); 
        #print l; 
        exax.append(float(l[0])); 
        exay.append(float(l[1]));
        exaerr.append(float(l[2]));


for line in holo.readlines():
    if line.startswith('#'):
        print "skip"
    else:
        l = line.strip(',').split(','); 
        #print l; 
        exhx.append(float(l[0])); 
        exhy.append(float(l[1]));
        exherr.append(float(l[2]));
        
print 'done with experimental loading'; 
        
#Averaging of .fit values before they are used for analysis. 



'''
These quotes are if the simulation data has already been averaged


mda1 = []; 
j=1; 
li=[0]; 
for i in xrange(1, 50001):
    ax,y=np.loadtxt('/home/xov/mdmx/pdb_tar/mdma_1-50/mdmaFit/mdma_' + str(i)+'00.fit', skiprows=1, usecols=(0,2), unpack=True); 
    if j==1:
        li.append(i); 
        mda1 = np.column_stack((ax,y));
        j=2; 
    else: 
        a1=np.column_stack((mda1,y)); 
        li.append(i); 
print "done with apo loading";     
mdh1=[];
j=1; 
li2=[];

for i in xrange(1, 50001):
    hx,y2=np.loadtxt('/home/xov/mdmx/top_dcd/merged_mdmh_p53/mdmhFit/' + str(i) + '00.fit', skiprows=1, usecols=(0,2), unpack=True);
    if j==1:
        li2.append(i);
        mdh1 = np.column_stack((hx,y2));
        j=2; 
    else:
        mdh1=np.column_stack((mdh1,y2)); 
        li2.append(i);
print "done with holo loading"; 
#print len(li); 
#print len(mda1);                
#t=np.vstack((li,mda1));  
#print t.shape; 






yvala1=[]; yerra1=[];
for i in xrange(1, (len(mda1)+1)): 
    #print a[int(i)-1,1:]; 
    r2 = np.average(mda1[int(i)-1, 1:]); 
    s2 = np.std(mda1[int(i)-1, 1:]); 
    yvala1.append(float(r2)); 
    yerra1.append(float(s2));

yvalh1 = []; yerrh1 = []; 
for i in xrange(1, (len(mdh1)+1)): 
    r = np.average(mdh1[int(i)-1, 1:]); 
    s = np.std(mdh1[int(i)-1, 1:]);  
    yvalh1.append(float(r)); 
    yerrh1.append(float(s));  
    
print 'here is xs'; 
print len(ax); 
print len(hx); 



print 'ya yh'; 
print len(yvala1);
print len(yvalh1);  
print len(exhx); 
print len(exax); 

#np.savetxt('exhx.txt', exhx); 
#np.savetxt('exhy.txt', exhy); 
#np.savetxt('exherr.txt', exherr); 

q=np.savetxt('hxf.txt', hx); 
w=np.savetxt('yvalh1f.txt', yvalh1 ); 
e=np.savetxt('yerrh1f.txt', yerrh1 ); 

u=np.savetxt('axf.txt', ax ); 
o=np.savetxt('yvala1f.txt', yvala1 ); 
p=np.savetxt('yerra1f.txt', yerra1 );
'''

hx=np.loadtxt('hxf.txt' ); 
yvalh1=np.loadtxt('yvalh1f.txt'  ); 
yerrh1=np.loadtxt('yerrh1f.txt' ); 

ax=np.loadtxt('axf.txt'  ); 
yvala1=np.loadtxt('yvala1f.txt' ); 
yerra1=np.loadtxt('yerra1f.txt' );









#plot of MD-apo, MD-holo, Exp-apo, Exp-holo;     
plt.loglog(hx, yvalh1, alpha=0.6); 
plt.errorbar(hx, yvalh1, yerrh1, alpha=0.6, marker='',ls=':', linewidth=3.0,  color='m', label='Simulation MDMX-p53');
plt.loglog(ax,yvala1, alpha=0.6);
plt.errorbar(ax,yvala1, yerra1, alpha=0.6, marker='', ls=':', linewidth=3.0,  color='c', label='Simulation MDMX')        
plt.loglog(exhx, exhy); 
plt.errorbar(exhx, exhy, exherr, marker='*',  color='k', label='Experimental MDMX-p53');
plt.loglog(exhx,exhy);
plt.errorbar(exax,exay, exaerr, marker='*',  color='r', label='Experimental MDMX');            
plt.xlim([0.015, 0.45]);
plt.ylim([0, 0.1]); 
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title(' I(Q) vs. Q', fontsize=25); 
plt.legend(loc=3); 
plt.show();                
                    
                        
                            
                                
                                    
                                            
#plt.errorbar(x, y, yerr); Plot of MD apo vs MD holo
plt.loglog(hx, yvalh1); 
plt.errorbar(hx, yvalh1, yerrh1, marker='*', linewidth=1.0, color='r', label='MD MDMX-p53');
plt.loglog(ax,yvala1);
plt.errorbar(ax,yvala1, yerra1, marker='*', linewidth=1.0, color='k', label='MD MDMX'); 
plt.xlim([0.015, 0.45]);
plt.ylim([0, 0.1]); 
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title(' Simulation I(Q) vs. Q', fontsize=25); 
plt.legend(loc=3); 
#plt.show(); 

#plt.errorbar(x, y, yerr); Plot of Exp apo vs Exp holo
plt.loglog(exhx, exhy); 
plt.errorbar(exhx, exhy, exherr, marker='*', linewidth=1.0, color='r', label='EXP MDMX-p53');
plt.loglog(exhx,exhy);
plt.errorbar(exax,exay, exaerr, marker='*', linewidth=1.0, color='k', label='EXP MDMX'); 
plt.xlim([0.015, 0.45]);
plt.ylim([0, 0.1]); 
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title('Experimental I(Q) vs. Q', fontsize=25); 
plt.legend(loc=3); 
#plt.show(); 

#plt.errorbar(x, y, yerr); Experimental Apo with simulation apo
plt.loglog(ax,yvala1);
plt.errorbar(ax,yvala1, yerra1, marker='*', linewidth=1.0, color='r', label='MD MDMX');
plt.loglog(exax,exay);
plt.errorbar(exax,exay, exaerr, marker='*', linewidth=1.0, color='b', label='EXP MDMX'); 
plt.xlim([0.015, 0.45]); 
plt.ylim([0, 0.02]);
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title('Apo I(Q) vs. Q', fontsize=25); 
plt.legend(loc=3); 
#plt.show();    

#plt.errorbar(x, y, yerr);  Experimental holo with simulation holo
plt.loglog(hx, yvalh1); 
plt.errorbar(hx, yvalh1, yerrh1, marker='*', linewidth=1.0, color='r', label='MD MDMX-p53');
plt.loglog(exhx, exhy); 
plt.errorbar(exhx, exhy, exherr, marker='*', linewidth=1.0, color='b', label='EXP MDMX-p53'); 
plt.xlim([0.015, 0.45]); 
plt.xlabel("Q", fontsize=19); 
plt.ylabel("I(Q)", fontsize=19);
plt.grid(True); 
plt.title('Holo I(Q) vs. Q', fontsize=25); 
plt.legend(loc=3); 
#plt.show();       









