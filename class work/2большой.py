from itertools import *

def f1(w,x,y,z):
    return ((x<=y) == (w or (not(z))))
def f2(w,x,y,z):
    return ((x<=y) and ((not(w))==z))
for c in product([0,1], repeat = 3):
    table = [(c[0],1,0,1), (c[1],0,0,0), (0,c[2],0,0)]
    if len(table)==len(set(table)):
        for p in permutations('xywz'):
            if f2(**dict(zip(p, table[0])))==0 and f1(**dict(zip(p, table[1])))==0 and f1(**dict(zip(p, table[2])))==0 and f2(**dict(zip(p, table[2])))==1:
                print(p, table)
                