import itertools

counter = itertools.repeat(2)


squares = map(pow, range(10), counter)


print(list(squares))
