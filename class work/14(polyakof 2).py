#p = 0
for x in range(0, 11):
    for y in range(0, 11):
        f = (7 * 25 ** 5 + y * 25 ** 4 + 2 * 25 ** 3 + 3 * 25 ** 2 + x * 25 ** 1 + 5 * 25 ** 0) + (6 * 11 ** 4 + 7 * 11 ** 3 + x * 11 ** 2 + 9 * 11 ** 1 + y * 11 ** 0)
        if f % 131 == 0:
            print(x, y, f // 131)
# правильный ответ 552647