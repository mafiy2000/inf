for a in range(0, 1000):
    flag = True
    for x in range(0, 200):
        f = (((x & 35 != 0) and (x & 15 == 0)) <= ((x & 15 == 0) <= (x & a != 0)))
        if f == 0:
            flag = False
            break
    if flag == True:
        print(a)
        break
# в range первое число зависит от условия, второе на абум главное побольше 100