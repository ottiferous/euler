import time
start = time.time()

count = 0
result = 0
limit = 1000000

collatzmemo = {}
collatzmemo[1] = 3
collatzmemo[2] = 1

for pos in xrange(2, limit):
    num = 0
    x = pos
    
    while x != 1:

        if not x in collatzmemo:
            if x % 2 == 0:
                x = x / 2
            else: x = 3*x + 1
            num += 1

            if x in collatzmemo:
                num += collatzmemo[x]
                collatzmemo[pos] = num
                x = 1
        else:
            num = collatzmemo[x]
            break

    if num > count:
        count = num 
        result = pos

    if ( pos % 100000 ) == 0:
        print "Finished " + str(pos) + " numbers"

print "Highest count is: " + str(count) + " for number: " + str(result)
print "In " + str(time.time()-start) + " seconds"
