import time

#   Gets pyramid from file and retuns linear array
def getpyramid():
    biglist = "" 

    for line in open ('18list', 'r'):
        biglist += line

    a = biglist.split()

    count = 0
    list = []
    for num in a:
        list.append(int(num))
        count += 1

    return list

#   returns the number of rows starting
#   at one in a pyramid of arbitrary size
def pyramidrows(num):
    row = 0
    while row != num:
        num -= row
        row += 1 
    return row

#   find first element in array for Nth row
def getrow(n):
    count = 0
    for _ in xrange(n):
        count += _
    return count

#   sum row of node paths
def rowsums(row):
    mod_row = []
    for x in row:
        mod_row[x]
    
    
#   sum the paths immediately below a node
def pathsum(node):
    return

start = time.time()
pyramid = getpyramid()
size = pyramidrows
