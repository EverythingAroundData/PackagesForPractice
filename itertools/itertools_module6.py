import itertools

names = ['Mridul', 'Tushar', 'Dhruva', 'Garvesh',
         'Anurag', 'Chander', 'Garvit', 'Anil',
         'Shyam', 'Sandeep', 'Upasana', 'Priyanka',
         'Shruti', 'Mohita', 'Deepak', 'Naveen',
         'Akankshya']


#List slicing - the stupid way

result = itertools.islice(names, 5, 12)

for item in result:
    print(item)

#List slicing - the stupid way
result = itertools.islice(names, 5, 12, 2)

for item in result:
    print(item)

#List slicing - the normal way
print(names[5:12])

print(names[5:12:2])


#reading file header the itertools way
with open('info.txt', 'r') as f:
    header = itertools.islice(f, 2)
    for line in header:
        print(line, end='')

print('\n')

#reading file header the normal way
with open('info.txt', 'r') as f:
    header = f.readlines()[:4]
    for line in header:
        print(line, end = '')
