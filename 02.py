result = 0
n = 0
f = core.fib()
while n < 4000001:
    n = f.next()
    if n % 2 == 0: result += n
print result