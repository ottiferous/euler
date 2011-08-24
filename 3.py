import core
start = core.time()

a = core.divisors(600851475143)
a.sort()
a.reverse()
result = 0

for num in a:
    if core.isprime(num):
        result = num
        break
    
print "Largest Prime Factor is: " + str(result)
print "Elapsed time " + str(core.time()-start) + " seconds"
