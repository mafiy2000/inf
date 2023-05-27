from itertools import *

def f(x,y,z,w):
    return (((y<=x)==(x<=w)) and (z or x))

for c in product([0,1], repeat = 6):
    t = [(0,c[0],c[1],0), (0,0,0,c[2]), (c[3],c[4],0,c[5])]
    if len(t) == len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [1,1,1]:
                print(p)