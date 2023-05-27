def f(s1, s2, c,m):
    if s1 + s2 > 60: return c%2==m%2
    if c==m: return 0
    if s1>s2:
        h = [f(s1+1,s2,c+1,m), f(s1,s2+2,c+1,m), f(s1,s2*2,c+1,m)]
    else:
        h = [f(s1+1,s2,c+1,m), f(s1+2,s2,c+1,m), f(s1*2,s2,c+1,m)]
    return any(h) if (c+1)%2==m%2 else all(h)

for s in range(1,53):
    for m in range(1, 5):
        if f(8,s,0,m):
            print(s,m)
            break
