for a in range(0, 1000):
    flag = True
    for x in range(0, 200):
        for y in range(1, 200):
            f = ((y ** 2 < a) <= (y <= 14)) and ((x <= 13) <= (x ** 2 < a))
            if f == 0:
                flag = False
                break
    if flag == True:
        print(a)
        break