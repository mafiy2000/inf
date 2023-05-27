def pr(n):
    md = cl(n**0,5)
    if n%md==0:
        l=[md]
    else: l=[]

    for k in range(2, md):
        if n%k==0:
            l.append(k)
            l.append(n//k)
    if len(l)==0: return True
    else: return False