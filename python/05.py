seed = 19*17*13*11
test = reduce(lambda x, y: x*y, xrange(2, 20)
count = 1

while seed < test:
	if all(seed*count % n == 0 for n in xrange(2, 20)):
		print "Result is: " + str(seed*count)
		break
	count += 1
