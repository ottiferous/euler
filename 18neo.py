def get_pyramid(filename):
    
    string_list = ""
    for line in open(filename, 'r'):
        string_list += line

    string_list = string_list.strip().split('\n')
    string_list.reverse()
    return [[int(x) for x in row.split()] \
        for row in string_list]

def max_path():
    triangle = get_pyramid('18list')

    max_list = []
    max_list.append(triangle[0])

#
#   Something in this code block causes it to go out of range
#   during the indexing of triangle
#
#   Reducing the range by 1 on both loops still has it going out of range!?
#
#       max_list = triangle[row][x] + max(max_list[x], max_list[x+1]) # goes out of range?
#
#   max_list is not an array!?

    for row in range(len(triangle)):
        for x in range(len(triangle[row])-1):            
            max_list = triangle[row][x] + max(triangle[row][x], triangle[row][x+1]) # goes out of range?

    return max_list
