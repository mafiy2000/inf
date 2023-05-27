import csv
f = open('9_123_.csv')
s = csv.reader(f, delimiter = ',')
count = 0
for x in s:
    flag1 = 1
    for i in range(2):
        if int(x[i])+int(x[i+2])!=180:
            flag1 = 0
            break
    if flag1 == 1:
        count += 1
print(count)
