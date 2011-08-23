from math import factorial

#   Find any number in Fibonnacci sequence using nCr
#
#
grid = 20
n = grid*2
r = grid

result = ((factorial(n))/(factorial(r)*(factorial(n-r))))

print result


