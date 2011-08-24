from math import factorial
from time import time
start = time()

grid = 20
n = grid*2
r = grid

result = ((factorial(n))/(factorial(r)*(factorial(n-r))))

print result
print "Elapsed time: " + str(time() - start)
