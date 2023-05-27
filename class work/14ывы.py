for p in range(7, 100):
    for x in range(1, p):
        for y in range(1, p):
            for z in range(1, p):
                if y * p ** 2 + 4 * p ** 1 + y * p ** 0 + y * p ** 2 + 6 * p ** 1 + 5 * p ** 0 == x * p ** 3 + z * p ** 2 + 2 * p ** 1 + 3 * p ** 0:
                    print(x, y, z)
                    print(x * p ** 2 + y * p ** 1 + z * p ** 0)
                    break