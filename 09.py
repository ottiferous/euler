a, b, c = 3,4,5
for a in range(3,500):
	for b in range(a+1,500):
		for c in range(b+1,500):
			if (c*c) == (b*b + a*a):

				if (a+b+c) == 1000:
					break
		if a+b+c == 1000:
			break
	if a+b+c == 1000:
		break
