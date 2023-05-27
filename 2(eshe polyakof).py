from itertools import permutations, product

def f (x,y,z):
    return (((not x) and y and z) or ((not x) and (not z)))

t = [(0, 0, 0), (1, 0, 0), (1, 1, 0)]
if len(t) == len(set(t)):
    for p in permutations('xyz'):
        if [f(**dict(zip(p, row))) for row in t] == [1, 1, 1]:
            print('answer', p)