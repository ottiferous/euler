import core

primes = core.primelist(xrange(0, 2000000))
hold = 0
for i in primes:
	hold += i
print "Summation is: " + str(hold)
