#   If the numbers 1 to 5 are written out in words: one, two, three, four, five, 
#   then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#
#   If all the numbers from 1 to 1000 (one thousand) inclusive 
#   were written out in words, how many letters would be used?
from time import time

numdict = {
    0   :   "",
    1   :   "one",
    2   :   "two",
    3   :   "three",
    4   :   "four",
    5   :   "five",
    6   :   "six",
    7   :   "seven",
    8   :   "eight",
    9   :   "nine",
    10  :   "ten",
    11  :   "eleven",
    12  :   "twelve",
    13  :   "thirteen",
    14  :   "fourteen",
    15  :   "fifteen",
    16  :   "sixteen",
    17  :   "seventeen",
    18  :   "eighteen",
    19  :   "nineteen",
    20  :   "twenty",
    30  :   "thirty",
    40  :   "forty",
    50  :   "fifty",
    60  :   "sixty",
    70  :   "seventy",
    80  :   "eighty",
    90  :   "ninety",
    100 :   "hundred",
    1000:   "thousand"
}

#   find the letters of a given number
def lettersof(number):

    if number < 21:
        return len(numdict[number])
    if number == 1000:
        return len(numdict[number]) + len("one")
    i = word = 0

    #i = int(number/1000)
    #if i > 0:
        #word += len(numdict[i]) + len(numdict[1000])
    #number -= i*1000
    
    i = int(number/100)
    if i > 0:
        word += len(numdict[i]) + len(numdict[100]) + len("and")
    number -= i*100
    
    i = int(number/10)
    if i > 0:
        word += len(numdict[i*10])
    number -= i*10

    word += len(numdict[number])

    return word

#   Now begins the actual code

start = time()

count = 0
for num in range(1, 1001):
    count += lettersof(num)

print count
print "Elapsed time: " + str((time() - start)*1000)
