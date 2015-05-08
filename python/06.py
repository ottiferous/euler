sumofsquare = 0
squareofsum = 0


for count in range(100):
	sumofsquare += (count**2)
	squareofsum += count
	
squareofsum = squareofsum**2
print str(squareofsum - sumofsquare)
