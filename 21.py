from time import time
from core import divisors

def prob21(ceiling):
    start = time()
    
    result = 0

    for num in range(1, ceiling+1):

        a = sum(divisors(num))-num
        if num == (sum(divisors(a))-a):
            result += num

    print "Elapsed time: " + str((time() - start)/100)
    return result


print prob21(10000)
