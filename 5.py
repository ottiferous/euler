from math import factorial
from time import time

start = time()
seed = 19*17*13*11
test = factorial(20)
count = 1

while seed < test:
	if ((seed*count) % 20 == 0) \
		and ((seed*count) % 19 == 0) \
		and ((seed*count) % 18 == 0) \
		and ((seed*count) % 17 == 0) \
		and ((seed*count) % 16 == 0) \
		and ((seed*count) % 15 == 0) \
		and ((seed*count) % 14 == 0) \
		and ((seed*count) % 13 == 0) \
		and ((seed*count) % 12 == 0) \
		and ((seed*count) % 11 == 0) \
		and ((seed*count) % 10 == 0) \
		and ((seed*count) %  9 == 0) \
		and ((seed*count) %  8 == 0) \
		and ((seed*count) %  7 == 0) \
		and ((seed*count) %  6 == 0) \
		and ((seed*count) %  4 == 0) \
		and ((seed*count) %  3 == 0) \
		and ((seed*count) %  2 == 0): 
			print "Result is: " + str(seed*count)
			break
	count += 1
print "Elapsed time: " + str(time() - start)
