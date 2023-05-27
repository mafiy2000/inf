def f(x):
    N = bin(x)[:2]
    ch = len([d for d in str(x) if d in '02468'])
    nch = len(str(x)) - ch
    if nch == (nch%3==0): N = N + '1'
    if N == ch : N = N + '0'
    return int(2,N)
print()