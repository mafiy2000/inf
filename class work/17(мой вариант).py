# прочитали и сохранили
f = open('17.txt')
a = []
for x in f:
    a.append(int(x))
# сколько делится на 3
c3 = 0
for x in a:
    if x % 3 == 0:
        c3 += 1
# сколько нужных чисел
count = 0
for k in range(len(a)-1):
    if (a[k]<0 or a[k+1]<0) and (a[k] + a[k+1]<c3):
        count += 1
print(count, c3)