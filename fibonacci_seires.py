
from calendar import c


a = 0
b = 1

print(a, b, end = ' ')

i = 1

for i in range(8):
    c = a + b
    print(c, end = ' ')
    a = b
    b = c
    i += 1