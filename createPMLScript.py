import os, string, sys

f = open(sys.argv[1], 'r');
count  = 0;
for line in f.readlines():
	if count%100 == 0:
		print 'load ' + line.strip();
	count = count + 1;
f.close();
