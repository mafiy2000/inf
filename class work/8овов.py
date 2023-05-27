from itertools import *
k = 0
for i in product("АВЛОР", repeat = 4):
    b = ''.join(i)
    k += 1
    if b[0]== 'Л':
        print(k, b)
        break
