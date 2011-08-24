from time import time

#   Calculate time elapsed in program
def deltatime():
    start = time()
    while True:
        yield time() - start


#   Checks if arguent is prime  
def isprime(n):
    n = abs(int(n))
    if n < 2:
        return False
    if n == 2: 
        return True
    if not n & 1:
        return False
    for x in xrange(3, int(n**0.5)+1, 2):
            if n % x == 0:
                    return False
    return True 

#   Returns a list of primes based on a range
def primelist(span):
    primes = []
    for x in span:
        if isprime(x):
            primes.append(x)
    return primes

#   Generates successive "triangle" numbers
def trigen():
    n = 1
    while True:
            yield int(((n*(n+1))/2))
            n += 1

#   Returns number of divisors for a given number
def numofdivs(n):
    count = 2
    for x in xrange(2, int(n**0.5)+1):
        if ((n % x) == 0):
            if (x != (n**0.5)) : count += 2
            else: count += 1
    return count

#   Returns a list of divisors for a given number
def divisors(num):
    divlist = [1]
    for x in xrange(2, int(num*0.5)+1):
        if ((num % x) == 0):
            divlist.append(int(x))
            divlist.append(int(num/x))
    divlist.append(num)

    result = list(set(divlist))
    result.sort()
    return result

#   Recursive Prime Generator (R.P.G.)
def RPG(start = 2):
    pos = start
    while True:
        if numofdivs(pos) == 2:
            yield pos
        pos += 1

#   Returns the count of the supplied number
def collatz(num):
    count = 0 
    while num != 1:
        if ( num % 2 ) == 0:
            num = num / 2
        else: num = (3 * x) + 1
        count += 1
    return count

#   Collatz Map Generator with memoization
def CollatzMap(span):
    memo = {}
    for pos in span:
        num = 0
        x = pos

        while x!= 1:

            if not x in memo:
                if x % 2 == 0:
                    x = x / 2
                else: x = (3 * x) + 1
                num += 1

                if x in memo:
                    num += memo[x]
                    memo[pos] = num
                    x = 1
            else:
                num = memo[x]
                break

        if num > count:
            count = num
            result = pos
    
#   Recursive Fibonacci Generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b
