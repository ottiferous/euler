from time import time
#   Returns a list of divisors for a given number
#   Modified from core to exclude the number itself
def divisors(num):
    divlist = [1]
    for x in xrange(2, int(num**0.5)+1):
        if ((num % x) == 0):
            divlist.append(int(x))
            divlist.append(int(num/x))

    result = list(set(divlist))
    result.sort()
    return result

#   Abundant Num (max out at 28123)
def abundnum(max):
    
    nums = []
    for x in range(1, max):
        if sum(divisors(x)) > x:
            nums.append(x)
    return nums

#   Finds all possible sums of the numbers in an array
def sum_variations(nums):
    
    big_list = []

    for each in nums:
        for item in nums:
            big_list.append(item + each)

    return list(set(big_list))
   
#   Filter out the numbers in sieve from list 
def filter(source, sieve):
   
   return list(set(source) - set(sieve))

#   Run the program
def proj23():
    
    start = time()
    nums = abundnum(28123)
    sieve = sum_variations(nums)

    answer = filter(range(1, 28124), sieve)
    print "- *23* Elapsed Time: *" + str((time() - start)*1000) + "*"

    return sum(answer)
