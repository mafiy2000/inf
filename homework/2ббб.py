from itertools import *
def f(x,y,z,w):
    return (((not(y)) <= (z == w)) and ((z <= x) == w))

for c in product([0,1], repeat = 2):
    t = [(1,1,0,1), (0,1,1,1), (0,c[0],c[1],0)]
    if len(t) == len(set(t)):
        for p in permutations("xyzw"):
            if [f(**dict(zip(p, row))) for row in t] == [1,1,1]:
                print(p)
