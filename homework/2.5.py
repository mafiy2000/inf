from itertools import *
def f(x,y,z,w):
    return ((w <= x) and ((y <= z) == (x <= y)))
for c in product([0,1], repeat = 4):
    t = [(0,1,1,0), (1,c[0],c[1],0), (c[2], 1,0,c[3])]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [1,1,1]:
                print(p)