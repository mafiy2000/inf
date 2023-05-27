from itertools import *
def f(x,y,z):
    return ((z==y) or ((y or z) <= x))
for c in product([0,1], repeat = 3):
    t = [(c[0],1,1), (c[1],c[2],1)]
    if len(t)==len(set(t)):
        for p in permutations('xyz'):
            if [f(**dict(zip(p, row))) for row in t] == [0,0]:
                print(p)