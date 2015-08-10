#Gromacs automation for one file at a time.

import sys, os
import subprocess
from subprocess import *
import shutil


path = (sys.argv[1]); #path to directory with pdb files 

dirlist = os.listdir(path); 

"""
Notation for naming simplicity: 
    A = AMBER
        Followed by number + further ID
            i.e. 
    C27 = CHARMM27
    G = GROMOS
        Followed by four digit ID
            i.e. G43a1 = GROMOS96 43a1
    OP = OPLS-AA/L
"""    




for i in dirlist:
    split = i.split('.');
    fname = split[0];
    
    
    os.mkdir(str(fname) + 'amber03');
    path1 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber03')    
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber03 -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A03'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A03'+'.top' + ' '+ '-water tip3p');  #Amber03                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A03'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A03'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');  
    os.system( 'mv' + ' '+ '*.top' + ' ' + str(path1));
    os.system( 'mv' +' ' + '*.gro' + ' ' + str(path1)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path1));
    
    os.mkdir(str(fname) + 'amber99');
    path2 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99 -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99'+'.top' + ' '+ '-water tip3p'); #Amber99                                                                      
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path2));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path2)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path2));
    
    os.mkdir(str(fname) + 'amber99sb');
    path3 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99sb')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99sb -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99SB'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99SB'+'.top' + ' '+ '-water tip3p');  #Amber99SB                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99SB'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99SB'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path3));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path3)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path3));
    
   
    
    os.mkdir(str(fname) + 'amber99sb-ildn');
    path4 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99sb-ildn')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99sb-ildn -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99SB-ILDN'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99SB-ILDN'+'.top' + ' '+ '-water tip3p');   #Amber99sb-ildn                                                                   
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99SB-ILDN'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99SB-ILDN'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path4));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path4)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path4));
    
    
    
    os.mkdir(str(fname) + 'amber99sb-star');
    path5 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99sb-star')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99sb-star -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99SB-star'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99SB-star'+'.top' + ' '+ '-water tip3p');   #Amber99sb-star                                                                   
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99SB-star'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99SB-star'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path5));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path5)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path5));
    
    os.mkdir(str(fname) + 'amber99sb-star-ildn');
    path6 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99sb-star-ildn')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99sb-star-ildn -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99SB-star-ILDN'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99SB-star-ildn'+'.top' + ' '+ '-water tip3p');  #Amber99sb-star-ILDN                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99SB-star-ILDN'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99SB-star-ILDN'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path6));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path6)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path6));
    
    os.mkdir(str(fname) + 'amber99sb-star-ildnp');
    path7 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'amber99sb-star-ildnp')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff amber99sb-star-ildnp -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'A99SB-star-ildnP'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'A99SB-star-idlnP'+'.top' + ' '+ '-water tip3p');  #Amber99sb-star-ildnp                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'A99sb-star-idlnP'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'A99SB-star-ildnP'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path7));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path7)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path7));
    
    os.mkdir(str(fname) + 'charmm27');
    path8 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'charmm27')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff charmm27 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'C27'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'C27'+'.top' + ' '+ '-water tip3p');  #charmm27                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'C27'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'C27'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path8));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path8)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path8));
    
    os.mkdir(str(fname) + 'gromos43a1');
    path9 = ('/home/xov/IDPs/p15/' + str(fname) + 'gromos43a1')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos43a1 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G43a1'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G43a1'+'.top' + ' '+ '-water tip3p');  #Gromos96 43a1                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G43a1'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G43a1'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path9));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path9)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path9));
    
    os.mkdir(str(fname) + 'gromos43a2');
    path10 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'gromos43a2')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos43a2 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G43a2'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G43a2'+'.top' + ' '+ '-water tip3p');  #Gromos96 43a2                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G43a2'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G43a2'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path10));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path10)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path10));
    
    os.mkdir(str(fname) + 'gromos45a3');
    path11 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'gromos45a3')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos45a3 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G45a3'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G45a3'+'.top' + ' '+ '-water tip3p');  #Gromos96 45a3                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G45a3'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G45a3'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path11));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path11)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path11));
    
    os.mkdir(str(fname) + 'gromos53a5');
    path12 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'gromos53a5')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos53a5 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G53a5'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G53a5'+'.top' + ' '+ '-water tip3p');  #Gromos96 53a5                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G53a5'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G53a5'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path12));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path12)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path12));
    
    os.mkdir(str(fname) + 'gromos53a6');
    path13 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'gromos53a6')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos53a6 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G53a6'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G53a6'+'.top' + ' '+ '-water tip3p');  #Gromos96 53a6                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G53a6'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G53a6'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path13));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path13)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path13));
    
    os.mkdir(str(fname) + 'gromos54a7');
    path14 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'gromos54a7')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff gromos54a7 -f' + ' ' + str(i) +' '+ '-o'+ ' ' + str(fname)+'G54a7'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'G54a7'+'.top' + ' '+ '-water tip3p');  #Gromos96 54a7                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'G54a7'+'.gro'+ ' ' + '-o' + ' ' + str(fname)+'G54a7'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2');
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path14));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path14)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path14));
    
    os.mkdir(str(fname) + 'opls');
    path15 = ('/home/xov/IDPs/p15/6AAA-4813/' + str(fname) + 'opls')
    os.system('/home/xov/gromacs/bin/pdb2gmx' + ' ' + '-ignh -ff oplsaa -f' + ' ' + str(i) +' '+ '-o' + ' ' + str(fname)+'OPLS'+'.gro'+ ' ' + '-p' + ' ' + str(fname)+'OPLS'+'.top' + ' '+ '-water tip3p');  #OPLS-AA/L                                                                    
    os.system('/home/xov/gromacs/bin/editconf' + ' ' + '-f' + ' ' +str(fname)+'OPLS'+'.gro' + ' ' + '-o' + ' ' + str(fname)+'OPLS'+'-PBC'+'.gro'+ ' ' + '-bt cubic -d 1.2'); 
    os.system( 'mv' + ' ' + '*.top' + ' ' + str(path15));
    os.system( 'mv' + ' ' + '*.gro' + ' ' + str(path15)); 
    os.system( 'mv' + ' ' + '*.itp' + ' ' + str(path15));
    
