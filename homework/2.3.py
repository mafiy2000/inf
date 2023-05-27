from itertools import *
def f(x,y,z,w):
    return (((y<=z) or (not(x)and w)) == (w == z))
for c in product([0,1], repeat = 3):
    t = [(c[0],1,0,0), (0,0,0,1), (0,1,c[1],c[2])]
    if len(t)==len(set(t)):
        for p in permutations('xyzw'):
            if [f(**dict(zip(p, row))) for row in t] == [1,1,1]:
                print(p)