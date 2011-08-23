#   Recursive Fibonacci Generator
def fib():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

result = "test"
count = 0

for x in fib():
    result = str(x)
    if len(result) == 1000:
        break
    count += 1

print count




