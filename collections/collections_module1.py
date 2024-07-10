from collections import namedtuple

def custom_divmod(x, y):
    divm = namedtuple('Divmod', 'Quotient,Remainder')
    return divm(*divmod(x,y))

#print(custom_divmod(12,5))

result = custom_divmod(12, 5)

print('Quotient :', result.Quotient)
print('Remainder:', result.Remainder)
