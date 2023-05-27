def f(start, end):
    if start == end: return 1
    if start > end: return 0
    if start == 2 or start == 3 or start == 5 or start == 7 or start == 11 or start == 13 or start == 17 or start == 19 or start == 23 or start == 29 or start == 31: return 0
    return f(start + 1,end) + f(start + 2,end) + f(start * 3,end)
print(f(8,16)*f(16,32))