from itertools import *
def f(a,b,c,d):
    return (((a >= b) == c) and (not(d)) or (d >= (not(a))))
for c in product([0,1], repeat = 9):
    t = [(0,c[0],c[1],c[2]), (c[3],c[4],0,c[5]), (0,c[6],c[7],0), (0,c[8],0,0)]
    if len(t)==len(set(t)):
        for p in permutations('abcd'):
            [f(**dict(zip(p, row))) for row in t] == [0,0,0,0]
print(p)