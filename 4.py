def ispalindrome(num):
	a = str(num)

	if (a == a[::-1]):
		return True
	return False

#	get list of all possible 6 digit palindromes

count = 999*999
plist = []

while count > 100000:

	if(ispalindrome(count)):
		plist.append(count)
	count -= 1

llist = range (110, 999, 11)

for i in plist:
	
	for x in llist:
		if ((i % x) == 0) and (len(str(i/x))==3):
			print "Solution set (" + str(x) + "," + str(i/x) + ") for " + str(i)
			break	
	
		if ((i % x) == 0) and (len(str(i/x))==3):
			break

		print "checking factors of: " +str(i)

