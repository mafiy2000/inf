nums = '0123456789'
for d1 in nums:
    n = '1' + d1 + '26558'
    if int(n) % 4173 == 0:
        print(n)
for d2 in nums:

    for d1 in nums:
        n = '1' + d1 + '2655' + d2 + '8'
        if int(n) % 4173 == 0:
            print(n)
for d3 in nums:
    for d2 in nums:
        for d1 in nums:
            n = '1' + d1 + '2655' + d2 + d3 + '8'
            if int(n) % 4173 == 0:
                print(n)
for d4 in nums:
    for d3 in nums:
        for d2 in nums:
            for d1 in nums:
                n = '1' + d1 + '2655' + d2 + d3 + d4 + '8'
                if int(n) % 4173 == 0:
                    print(n)