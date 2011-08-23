import core
start = core.time()

ubound = input ('Find primes up to: ')

list = core.primelist(range(0, ubound))

hold = 0

for _ in list:
	hold += _	

print "Summation is: " + str(hold)
print "Elapsed time: " + str(core.time() - start) + " seconds"
