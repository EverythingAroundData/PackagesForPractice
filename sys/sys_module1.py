import sys

dct = {1:'Apple', 2:'Orange'}

lst =  [[i for i in range(5)] for i in range(3)]

print(lst)

print(sys.getsizeof(dct))
print(sys.getsizeof(lst))

for args in sys.argv:
    print(args)
