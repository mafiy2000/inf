def f(start,end):
    if start == end: return 1
    if start > end: return 0
    if start == 11 or start == 15: return 0
    return f(start + 1, end) + f(start * 2, end) + f(start + 3, end)
print(f(2,8) * f(8,20))