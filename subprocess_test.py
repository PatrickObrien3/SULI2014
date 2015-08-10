import sys, os
import subprocess
from subprocess import *

path = ('/home/xov/subprocess'); #path to directory with pdb files 
print path; 

dirlist = os.listdir(path); 
#for i in dirlist:
    #f = open(i);
#fname = fulname[:-4];
#subprocess.call('mkdir' + ' '+ str(fname)+ 'test'); 
    #subprocess.call('mv'+ ' ' + '*.top' + ' '+ str(fname)+ 'test'); 
print dirlist; 
#file = ('1fqy.pdb'); 
#f = open(fullname); 
#fname = file[:-4];

for i in dirlist:
    split1 = i.split('.' + '-');
    print split1; 
    
    #split2list = split1[0];
    #split2 = split2list.split('-');
    fname = split1[0];
    os.mkdir(str(fname) + 'amber03');
    path1 = ('/home/xov/subprocess/' + str(fname) + 'amber03');     
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber03 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'A03'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A03'+'.top' + ' '+ '-water tip3p');  #Amber03                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A03'+'.gro'+ ' ' +'-o' + ' '+ str(fname)+'A03'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2'); 
    os.system( 'mv' + ' '+ '*.top' + ' ' + str(path1));
    os.system( 'mv' +' ' + '*.gro' + ' ' + str(path1)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path1)); 


"""    
pathlist = os.listdir(sys.argv[1])
 

for file in pathlist: 
    Dlist = []; 
    f = open(file);
    fname = file[:-4];
    subprocess.call('mkdir' + ' '+ 'str(fname)'+ 'test');
    
"""    