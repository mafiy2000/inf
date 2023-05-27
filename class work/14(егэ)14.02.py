
for p in range(10, 100): #зависит от максимального числа в выражении
    for x in range(1, p):
        for y in range(1, p):
            if x * p ** 3 + x * p ** 2 + x * p ** 1 + 8 + 4 * p ** 3 + 3 * p ** 2 + x * p ** 1 + 9 == y * p ** 3 + y * p ** 2 + 0 * p ** 1 + 4:
                print(p, x, y)
                print(y * p ** 2 + y * p ** 1 + x)

