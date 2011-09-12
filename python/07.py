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
	i = 0
	a = []
	while len(a) < n:
		if isprime(i):
			a.append(i)
		i += 1
	return a


list = primelist(10001)