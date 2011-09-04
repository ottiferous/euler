import core

a = core.primelist(range(0,int((600851475143**0.5)+1)))
a.reverse()

for num in a:
    if 600851475143 % num == 0:
        result = num
        break
    
print "Largest Prime Factor is: " + str(result)
