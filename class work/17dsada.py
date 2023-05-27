a = [int(x) for x in open('17s.txt')]

m = min(x for x in a if str(x)[-1] == str(x)[-2])


ans = []
for i in range(len(a)-1):
    if (str(a[i])[-1] == str(a[i+1])[-2] or str(a[i])[-2] == str(a[i+1])[-1]) and \
        (a[i]%7==0) + (a[i+1]%7==0) == 1 and a[i]**2 + a[i+1]**2 <= m**2:
        ans.append(a[i]**2 + a[i+1]**2)
print(len(ans), max(ans))