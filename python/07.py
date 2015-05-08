import re


def isPrime(n):
    m = re.match( r'^1?$|^(11+?)\1+$', '1'*n) # matches if not prime
    if m:
        return False
    else:
        return True

count = 1
primeList = []

while(len(primeList) < 1001):
    if isPrime(count):
        primeList.append(count)
    count += 1

print primeList[1000] # 1001st prime number
