from itertools import permutations, product

def f (a,b,c):
    return (((not a) or b or (not c)) and (b or (not c)))

t = [(0, 0, 0), (0, 0, 1), (0, 1, 0), (0,1,1), (1,0,0), (1,0,1), (1,1,0), (1,1,1)]
if len(t) == len(set(t)):
    for p in permutations('abc'):
        if [f(**dict(zip(p, row))) for row in t] == [1, 0, 1, 0, 1, 1, 1, 1]:
            print('answer', p)