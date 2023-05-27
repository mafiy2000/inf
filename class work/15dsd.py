for a in range(0, 1000):
    flag = True
    for x in range(0,200):
        f = ((x&114 != 0 or x&94 != 0 ) <= ((x&73 == 0) <= (x&a != 0)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)
        break