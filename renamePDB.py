#rename pdb files
#make sure to remove all of the trajin files first; 

import sys, os
 




for i in xrange(1, 50000):
    j = i+1; 
    os.system('mv' + ' ' + str(i) + '.pdb' + ' ' + 'merged_' + str(j) + '.pdb')






"""
path = (sys.argv[1])
fileList = os.listdir(path); 
#print fileList; 


for i in fileList:
    l = i.strip().split('.');
    print l; 
    os.system('mv'+ ' ' + 'mdmh.' + l[1] + ' ' + 'mdmh_' + l[1] + '.pdb'); 
"""

#for i in (1, NumFiles)
 #   i = line.strip(.).split();
  #  os.system( 'mv', 'mdma.' + str(i), 'mdma_' + str(i) + '.pdb'); 
    