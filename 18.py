#   Test Values
from time import time

list = [[11,7,5,8],[3,6,9],[14,10],[1]]

#   Load the pyramid from a text file
def get_pyramid(filename):
    
    string_list = ""
    for line in open(filename, 'r'):
        string_list += line

    string_list = string_list.strip().split('\n')
    string_list.reverse()
    return [[int(x) for x in row.split()] \
        for row in string_list]

#   Pair the numbers off in an array
def pairs(list):

    i = iter(list)
    first = prev = i.next()
    for item in i:
        yield prev, item
        prev = item
#   Function to reduce an array by 1
#   returns the reduced array
def reduce(row):

    hold = []
    for each in pairs(row):
        hold.append(max(each))
    return hold

# Make the summation triangle
#   gets an upside-down pyramid
def reducerows(start):
    
    result = []
    for row in range(len(start)-1):

        start[row] = reduce(start[row])
        start[row+1] = map(lambda x,y: x+y, start[row], start[row+1])
        print start[row]    

    return start[-1]

def proj18():

    start = time()
    a = get_pyramid('18list')
    print a
    print reducerows(a)
    print "Elapsed time: " + str((time() - start)*1000)

