import itertools

count = 0
for each in itertools.permutations('0123456789'):
    count += 1
    if count == 1000000:
        print each
        print count


