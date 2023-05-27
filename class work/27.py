f = open('27-A.txt')
n = int(f.readline())
data = []
for x in f:
    data.append(int(x))
count = 0
for k in range(0,n-1):
    for j in range(k+1,n):
        if (data[k] * data[j]) % 10 ** 7 == 0 and (data[k] * data[j]) % 10 ** 8 != 0:
            count += 1
print(count)

