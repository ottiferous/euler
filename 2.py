import time
start = time.time()

def F(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a+b

result = 0
for n in F(4000000):
   if n % 2 == 0: result += n
print result
print "Completed in " + str(time.time() - start) + " seconds"
