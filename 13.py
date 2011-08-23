import time
start = time.time()
biglist = 0

for line in open ('euler13list', 'r') :
	biglist += int(line)

a = str(biglist)

print "Solution is: " + a[:10]
print "In " + str(time.time() - start) + " seconds."
