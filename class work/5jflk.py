for n in range(1,9):
    b = bin(n)[2:]
    b = int(b)
    if b%3==0: b == str(b + b[-1] + b[-2] + b[-3])
    if b%3!=0: b == b + (b%3)*2
    print(b)
