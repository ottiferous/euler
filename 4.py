import core

start = core.time()
count = 999*999
plist = []

while count > 100000:

	if(core.ispalindrome(str(count))):
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
print "Elapsed time: " + str(core.time() - start)
