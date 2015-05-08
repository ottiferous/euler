a, b, c = 3, 4, 5

def pythTripletGenerator():
    for a in xrange(3, 500):
        for b in xrange(a+1, 500):
            for c in xrange(b+1, 500):
                if ((c**2 == b**2 + a**2) and (a+b+c == 1000)):
                    return (a, b, c)

print reduce(lambda x,y: x*y, pythTripletGenerator())
