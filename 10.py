import core

print "Finding the sum of all primes between 0 and 2.000.000"

list = core.primelist(range(0, 2000000))

hold = 0

for _ in list:
	hold += _	

print "Summation is: " + str(hold)
