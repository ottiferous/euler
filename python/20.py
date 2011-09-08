result = 0
for x in str(reduce(lambda x,y: x*y, xrange(1, 100), 1)):
    result += int(x)

print result
