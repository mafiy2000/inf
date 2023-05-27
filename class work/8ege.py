from itertools import permutations
num = 3*'n'+8*'c'
count = 0
l = permutations(num)
l = set(l)
for i in l:
    number = ''.join(i)
    if 'nn' not in number:
        if number[0] == 'n':
            count += 4 ** 11
        else:
            count += 3 * 4 ** 10
print(count)