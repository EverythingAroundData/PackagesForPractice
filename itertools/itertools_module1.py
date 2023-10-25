import itertools as it
import datetime as dttm
import time

counter = it.count()

t1 = dttm.datetime.now()
print(t1)
for num in counter:    
    #print(num)
    if num > 10000001:
        break

#time.sleep(5)
t2 = dttm.datetime.now()
print(t2)
print((t2-t1).seconds)



print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))