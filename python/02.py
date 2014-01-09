from core import fib
result = 0
n = 0
f = fib()
while n < 4000001:
    n = f.next()
    if n % 2 == 0: result += n
print result
