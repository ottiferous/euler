grid = 20
n = int(grid*2)
r = int(grid)

result = (reduce(lambda x,y: x*y, xrange(1, 40), 1))/(reduce(lambda x,y: x*y, xrange(1, 20), 1)*(reduce(lambda x,y: x*y, xrange(1, 20), 1)))

print result
