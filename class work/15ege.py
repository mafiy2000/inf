for a in range(0, 1000):
    flag = True
    for x in range(0, 100):
        f = (((x & 42 != 0) or (x&13 != 0)) <= ((x & 30 == 0) <= (x & a != 0)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)
        break