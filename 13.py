import time
start = time.time()
biglist = 0

for line in open ('13list', 'r') :
	biglist += int(line)

a = str(biglist)

print "Solution is: " + a[:10]
print "Elapsed time:" + str(time.time() - start)
