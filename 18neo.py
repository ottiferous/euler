#   Test Values

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
#    yield item, first

#   Sum the numbers in pairs
def sumrow(row):

    if(len(row) == 1): return row

    result = []
    for x in range(len(row)-1):
        result.append(row[x] + row[x+1])
    return result

# Make the summation triangle
#   gets an upside-down pyramid
def sum_pyramid(origin):
    
    new = []

#
#   This section will "sum" the pyramid and make the max-paths representation
#   the problem is that this does not correspond to the actual values - and a
#   method to find the index of a given array from the max of the modified array
#   and use the value in the original spot from the original array.
#
#   Its very confusing.
#
    new.append(origin[0])
    for row in range(1, len(origin)-1):
        new.append([i+j for i,j in zip(sumrow(origin[row-1]) ,origin[row])])
    
    new.append(origin[-1])

    return new

def proj18():
    a = []
    a = get_pyramid('18list')

    b = sum_pyramid(a)
    b.reverse()
    print b
    score = 0

    for row in range(len(b)):
        score += max(b[row])

    return score
