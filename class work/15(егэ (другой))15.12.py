for a in range(0, 1000):
    flag = True
    for x in range(1, 200):
        for y in range(1, 200):
            f = ((108 % x == 0) <= (x % y != 0)) or (x + y > 80) or (a - y > x)
            if f == 0:
                flag = False
                break
    if flag == True:
        print(a)
        break