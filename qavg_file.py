#q_array average
import numpy as np

numFiles = 50000
q_initial = np.loadtxt("1.array.gz"); 
qmatrix = q_initial*1; 
for i in range(2, numFiles):
    fname = str(i) + '.array.gz'; 
    f = np.loadtxt(fname); 
    qmatrix = np.add(qmatrix, f); 
    #print qmatrix; 

qavg = qmatrix/numFiles 
np.savetxt('qavg', qavg); 