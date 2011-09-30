import calendar

count = 0

for year in xrange(1901, 2001):

    for month in xrange(1, 13):

        if calendar.weekday(year,month,1) == 1:
            count += 1

print count


