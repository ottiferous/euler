from time import time
start = time()
bignum = 2**1000
result = 0
for x in str(bignum):
    result += int(x)

print result
print "Elapsed time: " + str(time() - start)
