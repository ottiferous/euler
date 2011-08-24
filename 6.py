from time import time

start = time()
sumofsquare = 0
squareofsum = 0

count = 1

for _ in range(100):
	sumofsquare += (count**2)
	squareofsum += count
	count += 1
	
squareofsum = squareofsum**2

print "Result is: " + str(squareofsum-sumofsquare)
print "Elapsed time: " + str(time() - start)
