from itertools import *
def f1(w,x,y,z):
    return ((x and not(y)) >= (w == z))
def f2(w,x,y,z):
    return (x and not(y) == (z >= w))

for c in product([0,1], repeat = 5):
    f = [(0,c[0],0,0), (c[1],1,1,c[2]), (c[3],0,0,0)]
    if len(f) == len(set(f)):
        for p in permutations('wxyz'):
            if f1(**dict(zip(p,f[0])))==0 and f2(**dict(zip(p,f[0])))==0 and