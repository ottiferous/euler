#
#   Screw summing it and using maths. Time for logic
#

#   Test Variables for loading into python repl

list = [[10], [11, 12], [13, 14, 15], [16, 17, 18, 19]]

#   Sum the numbers in pairs
def sumrow(row):
    
    if(len(row) == 1): return row

    result = []
    for x in range(len(row)-1):
        result.append(row[x] + row[x+1])
    return result

#   Gets pyramid from file and retuns list of each row
#       as a literal string. Returns pyramid upside-down
def getpyramid():

    biglist = []
    f = open('18list', 'r')

    for line in f.read().split('\n'):
        b = []
        for x in line:
            b.append(int(x))
        biglist.append(b)

    f.close()
    del biglist[-1]
    biglist.reverse()

    return biglist    #   returned array is 'upside-down'

#   Walk through the pyramid
#       takes the completed array
#       and finds the total score
def score(list):
   
    list.reverse()

    total = 0
    for row in list[:1]:
        total += max(sumrow(row))
    total += max(list[0])

    return total
