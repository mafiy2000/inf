from itertools import *
def f(x,y,z,w):
    return ((x and (not(y)) or (y == z) or not(w)))

for c in product([0,1], repeat = 4):
    table = [(0,c[0],c[1],0), (0,1,0,1), (c[2],1,0,c[3])]
    if len(table)==len(set(table)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in table] == [0,0,0]:
              print(p)