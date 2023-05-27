from itertools import *
def f(x,y,z,w):
    return ((x and y and z) >= (x or (y and w)))
for c in product([0,1], repeat = 4):
    table = [(1,0,c[0],0), (c[1],1,1,c[2]), (1,1,c[3],1)]
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            [f(**dict(zip(p,row))) for row in table]==[0,0,0]
