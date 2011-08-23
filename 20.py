from math import factorial
bignum = factorial(100)
result = 0
for x in str(bignum):
    result += int(x)

print result
