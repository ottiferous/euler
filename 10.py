def isprime(n):
	n = abs(int(n))
	if n < 2:
		return False
	if n == 2:
		return True
	if not n & 1:
		return False
	for x in range(3, int(n**0.5)+1, 2):
		if n % x == 0:
			return False
	return True

def primelist(n):
	a = []
	for i in range(2,n):
		if isprime(i):
			a.append(i)
	return a

ubound = input ('Find primes up to: ')

list = primelist(ubound)

hold = 0

for _ in list:
	hold += _	

print "Summation is: " + str(hold)
