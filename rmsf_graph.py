import numpy as np
import matplotlib as mpl
import pylab 
import matplotlib.pyplot as plt

def getArrayFromRMSF(fname):
    f = open(fname, 'r');
    i = 0;
    atomicFluctIndex =[];
    atomicFluctVals = [];
    for line in f.readlines():
            l = line.strip().split();
            i = i +1;
            if l[0][0] == '#':
                print line;
            else:
                atomicFluctIndex.append(i);
                atomicFluctVals.append(float(l[1]));
    f.close();
    return [atomicFluctIndex, atomicFluctVals];


#[AtomicIndex1, AtomicFluct1] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdma/mdma_1000ns/mdma_1_50000.out'); #apo; accidentilly got labeled 'mdmh'
[AtomicIndex2, AtomicFluct2] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_1000ns/mdmh_1_50000.out');



#
#Note: for mdma analysis of 50ns, errro was in naming so they are called mdmh files,
#but are in the data_mdma folder. 

[AtomicIndex3, AtomicFluct3] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_1_2500.out');
[AtomicIndex4, AtomicFluct4] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_2501_5000.out');
[AtomicIndex5, AtomicFluct5] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_5001_7500.out');
[AtomicIndex6, AtomicFluct6] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_7501_10000.out');
[AtomicIndex7, AtomicFluct7] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_10001_12500.out');
[AtomicIndex8, AtomicFluct8] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_12501_15000.out');
[AtomicIndex9, AtomicFluct9] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_15001_17500.out');
[AtomicIndex10, AtomicFluct10] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_17501_20000.out'); 
[AtomicIndex11, AtomicFluct11] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_20001_22500.out');  
[AtomicIndex13, AtomicFluct13] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_22501_25000.out');   
[AtomicIndex14, AtomicFluct14] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_25001_27500.out');
[AtomicIndex15, AtomicFluct15] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_27501_30000.out');
[AtomicIndex16, AtomicFluct16] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_30001_32500.out');
[AtomicIndex17, AtomicFluct17] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_32501_35000.out');
[AtomicIndex18, AtomicFluct18] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_35001_37500.out');
[AtomicIndex19, AtomicFluct19] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_37501_40000.out');
[AtomicIndex20, AtomicFluct20] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_40001_42500.out');
[AtomicIndex21, AtomicFluct21] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_42501_45000.out');
[AtomicIndex22, AtomicFluct22] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_45001_47500.out');
[AtomicIndex23, AtomicFluct23] = getArrayFromRMSF('/home/xov/mdmx/rmsf/data_mdmh/mdmh_50ns/mdmh_47501_50000.out');


   
      
         
            
               
                  
                        
#plt.plot(AtomicIndex1, AtomicFluct1, 'k-')    
plt.plot(AtomicIndex2, AtomicFluct2, 'k-')     
plt.plot(AtomicIndex3, AtomicFluct3, 'r-')
plt.plot(AtomicIndex4, AtomicFluct4, 'r-')
plt.plot(AtomicIndex5, AtomicFluct5, 'r-')
plt.plot(AtomicIndex6, AtomicFluct6, 'r-')
plt.plot(AtomicIndex7, AtomicFluct7, 'r-')
plt.plot(AtomicIndex8, AtomicFluct8, 'r-')
plt.plot(AtomicIndex9, AtomicFluct9, 'r-')
plt.plot(AtomicIndex10, AtomicFluct10, 'r-')
plt.plot(AtomicIndex11, AtomicFluct11, 'r-')
plt.plot(AtomicIndex13, AtomicFluct13, 'r-')
plt.plot(AtomicIndex14, AtomicFluct14, 'r-')
plt.plot(AtomicIndex15, AtomicFluct15, 'r-')
plt.plot(AtomicIndex16, AtomicFluct16, 'r-')
plt.plot(AtomicIndex17, AtomicFluct17, 'r-')
plt.plot(AtomicIndex18, AtomicFluct18, 'r-')
plt.plot(AtomicIndex19, AtomicFluct19, 'r-')
plt.plot(AtomicIndex20, AtomicFluct20, 'r-')
plt.plot(AtomicIndex21, AtomicFluct21, 'r-')
plt.plot(AtomicIndex22, AtomicFluct22, 'r-')
plt.plot(AtomicIndex23, AtomicFluct23, 'r-')



plt.savefig(filename='1000_50_test_holoblack_50red');
