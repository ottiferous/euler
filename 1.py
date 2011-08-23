import core

start = core.time()
mult3 = range (0, 1000, 3)
mult5 = range (0, 1000, 5)

dif = mult3 + mult5

result = 0

for i in set(dif) :
	result += i
    
print result
print "Elapsed time: " + str(core.time() - start) + " seconds"
