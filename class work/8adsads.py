from itertools import *
l = 0
for x in permutations('ВИКОРТ',):
    s = ''.join(x)
    l += 1
    if l == 266:
        print(x, l)
        break