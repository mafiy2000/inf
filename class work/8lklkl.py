from itertools import *
l=0
for i in product('АЕКРТ', repeat = 6):
    b = ''.join(i)
    l +=1
    print(b,l)