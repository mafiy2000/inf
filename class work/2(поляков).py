from itertools import permutations, product

def f (x,y,w,z):
    return (((x <= z) and (z <= w)) or (y == (x or z)))

for c in product([0,1], repeat = 7):
    t = [(c[0],1,c[1],c[2]), (c[3],c[4],1,1), (c[5],1,c[6],1)]
    if len(t) == len(set(t)):
        for p in permutations('xywz'):
            if [f(**dict(zip(p, row))) for row in t] == [0, 0, 0]:
                print('answer', p)
