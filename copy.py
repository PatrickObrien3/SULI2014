#copy to new folder for processing

import os, sys


#os.system('mkdir ../100k_Files'); 
#print 'made directory 100k_files'; 


for i in xrange(1, 2001):
    os.system('cp ' + str(i) + '00'+ '.int' + ' ' + '../IvsQtest/')
print 'done!'; 