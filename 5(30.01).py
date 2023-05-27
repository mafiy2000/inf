N = int(input())
N1 = 2 * N
N1b = bin(N1)
NS = N1b[2:]
sum = 0
for d in NS:
    sum += int(d)
    if sum % 2 == 0:
        NS = NS + '0'
print(NS)