import time
start = time.time()
from math import sqrt

def F(n):
    return int(((1+sqrt(5))**n-(1-sqrt(5))**n)/(2**n*sqrt(5)))

upper_limit = 4000000
count = 0
list = []

while F(count) <= upper_limit :
    list.append(F(count))
    count += 1

count = 0

list.pop(0)

for i in list :
    if (i % 2) == 0 :
        count += i

print count 
print (list)
print "In " + str(time.time() - start) + " seconds"

