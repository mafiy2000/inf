f = '0123456789'
for d1 in f:
    n = '1' + d1 + '39485'
    if int(n) % 3013 == 0:
        print(n)

for d1 in f:
    for d2 in f:
        n = '1' + d1 + '3948' + d2 + '5'
        if int(n) % 3013 == 0:
            print(n)

for d1 in f:
    for d2 in f:
        for d3 in f:
            n = '1' + d1 + '3948' + d2 + d3 + '5'
            if int(n) % 3013 == 0:
                print(n)

for d1 in f:
    for d2 in f:
        for d3 in f:
            for d4 in f:
                n = '1' + d1 + '3948' + d2 + d3 + d4 + '5'
                if int(n) % 3013 == 0:
                    print(n)