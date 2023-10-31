import itertools

counter = itertools.repeat(2)

#generate list of squares using map
squares = map(pow, range(10), counter)


print(list(squares))


#generate list of squares using itertool starmap  function
sqrs = itertools.starmap(pow, list(zip(range(10), counter)))

print(list(sqrs))
