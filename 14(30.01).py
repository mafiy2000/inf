m = 1000000000000000000000
for x in "0123456789ABCDEFG":
    a = int('10' + x + '0', 17) + int('F0'+ x + 'FF', 17)
    if a % 13 == 0:
        if a < m:
            m = a
print(m//13)
