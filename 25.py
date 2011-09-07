import core

result = "test"
count = 0
num = core.fib()
for x in num:
    result = str(x)
    if len(result) == 1000:
        break
    count += 1

print count
