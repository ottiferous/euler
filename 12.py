import time
start = time.time()

def trigen():
	n = 1
	while True:
		yield int(((n*(n+1))/2))	
		n += 1

def divisors(n):
	count = 2	# itself and one

	for i in xrange(2, int(n**0.5)+1):
		if ((n % i) == 0):
			if (i != (n**0.5)) : count += 2
			else: count += 1
	return count

answer = 0
trinum = trigen()

while True:
	num = trinum.next()
	if(divisors(num) > 500):
		answer = num
		break;
print "Answer is: " + str(answer)
print "Elapsed time: " + str((time.time() - start))
