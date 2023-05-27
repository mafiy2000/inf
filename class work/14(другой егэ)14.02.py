for p in range(10, 100):
    for x in range(1, p):
        for y in range(1, p):
            if 3 * p ** 3 + 2 * p ** 2 + x * p ** 1 + 8 * p ** 0 + x * p ** 3 + x * p ** 2 + x * p ** 1 + 9 * p ** 0 == y * p ** 3 + y * p ** 2 + 0 * p ** 1 + 2 * p ** 0:
                print(p, x, y)
                print(y * p ** 2 + y * p ** 1 + x * p ** 0)
