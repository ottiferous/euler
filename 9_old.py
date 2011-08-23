#	generate list of numbers evenly divisible into 500

mlist = []

for _ in range(1,500):
	if 500 % (_) == 0:
		mlist.append(_)

print mlist

for m in mlist:
	n = (500/m)-m
	if m > n:
		c = (m**2 + n**2)
		b = (2*m*n)
		a = (m**2 - n**2)

		print "(" + str(a) + "," + str(b) + "," + str(c) + ") -- sum: " + str(a+b+c)

		if (a+b+c == 1000) and ( a < b ) and ( b < c ):
			a = (m**2 - n**2)
			b = (2*m*n)
			c = (m**2 + n**2)
			print a*b*c
