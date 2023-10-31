import itertools

l1 = [1,2]
l2 = ['Mridul']
l3 = [{'k1':'Hello'}, {'k2':'World'}]
print(l1+l2+l3)




combined = itertools.chain(l1, l2, l3)


for item in combined:
    print(item)
