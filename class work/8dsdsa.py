from itertools import *

count = 0
for p in product('НЧ', repeat=11):
    w = "".join(p)
    if w.count('Н') == 4 and 'НН' not in w:
        if w[0] == 'Ч':
            count += 1
        else:
            count += 4 ** 11
print(count)
