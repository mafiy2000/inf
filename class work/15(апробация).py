def f(x,y):
    return (x+y<=32) or (y<=x+4) or (y>=a)

for a in range(100):
    if all(f(x,y)==1 for x in range(1,100) for y in range(1, 100)):
        print(a)