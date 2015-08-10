
#python loop to get run in the shiftx directory, placing files in that directory
# after the command and sys.argv[1] put '> shiftx_local.sh'
# then 'chmod +x shiftx_local.sh'
# then execute with ./shiftx_local.sh




import subprocess
import os, sys

path = (sys.argv[1]);

filelist = os.listdir(path); 

for f in filelist: 
    fname = f[:-4];
    print "/home/xov/shiftx/shiftx " +' ' + str(1) + " " + f + " " + fname+'.out' ; 






#path = (sys.argv[1]); 

#for file in (path):
#    fname = file[:-4]; 
 #   print ('./shiftx', '4', 'fname', '%s.out' % (fname));  
    
    
    
"""
    For number entry: 
1) Predict All Shifts (1H, 13C, 15N)
2) Predict Alpha 13C Shifts Only
3) Predict Carbonyl 13C Shifts Only
4) Predict Beta 13C Shifts Only
5) Predict Alpha 1H Shifts Only
6) Predict Amide 1H Shifts Only
7) Predict Amide 15N Shifts Only
"""    