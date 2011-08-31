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

# Make the summation triangle
#   gets an upside-down pyramid
def reducerows(start):
    
    result = []
    for row in range(len(start)-1):

        hold = []
        for each in pairs(start[row]):
            hold.append(max(each))

        print hold
        print start[row]
#       Not the same size when this is called....
        start[row] = map(lambda x,y: x+y, hold, start[row+1])

    return start

def proj18():
    a = []
    a = get_pyramid('18list')

    b = sum_row(a)
    b.reverse()
    print b
    score = 0

    for row in range(len(b)):
        score += max(b[row])

    return score
