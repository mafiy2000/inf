from itertools import *
k = 0
for x in product("АКРУ", repeat = 5):
    s = ''.join(x)
    k += 1
    if s[0] == 'К':
        print(k, s)
        break