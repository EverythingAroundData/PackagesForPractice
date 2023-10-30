import itertools

counter = itertools.count()

data = [100, 200, 300, 400]

daily_data = list(zip(counter, data))

print(daily_data)

dailydata = list(itertools.zip_longest(range(10), data))

print(dailydata)


cntr = itertools.count(start=5, step=-2.5)

for i in range(1,11):
    print(next(cntr))
