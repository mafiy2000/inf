from itertools import *
def f(x,y,z,w):
    return (((x or not(y))and (not(z) == w)) <= (y and z))
for c in product([0,1], repeat = 4):
    t = [(1,c[0],1,1), (0,0,c[1],0), (0,c[2],c[3],1)]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [0,0,0]:
                print(p)