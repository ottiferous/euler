bignum = reduce(int.__mul__, xrange(1, 100), 1)
result = 0
for x in str(bignum):
    result += int(x)

print result
