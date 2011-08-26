import time

#   Gets pyramid from file and retuns list of each row
def getpyramid(name):

    biglist = [] 
    f = open(name, 'r')
    for line in f.read().split('\n'):
        biglist.append(line)
    f.close()
    del biglist[-1]

    return biglist

#   Takes an array of characters to sum
#       returns a list of ints for that row
def sum(row):
    
    result = []
    for _ in xrange(len(row)-1):
        result.append((int(row[_])+int(row[_+1])))

    return result

#   sum values of row returning values to be
#       added to the row above in a 1:1 ratio
def makepaths(tri):

#   Need to start at the 'bottom' and work our way up
   tri.reverse()
   new = []

   for row in tri:
       new.append(sum(row))

