from time import time
import csv

# Get the names into an array for sorting
def getnames():

    a = []
    names = csv.reader(open('22list.txt', 'rb'), delimiter = ',', quotechar='"')
    for row in names.next():
        a.append(row)
    return a

#   Score the name based on its characters
def scoreof(name):

    score = 0
    for i in name:
        score = score + ord(i) - 64
    return score

#   Solve the Problem
def proj22():
    
    start = time()
    list = getnames()
    list.sort()

    points = 0
    for item in range(len(list)):
        points += (scoreof(list[item]) * (item+1))

    print "Elapsed time: " + str((time() - start)*1000)
    return points
