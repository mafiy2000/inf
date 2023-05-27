def f(start, end):
    if start == end:
        print('1',start, end)
        return 1
    if start < end:
        print('o',start, end)
        return 0
    if start%2 == 0 and start>=10:
        print('3',start, end)
        return f(start - 3,end) + f(start//3,end) + f(start//10,end)
    if start%2 == 0 and start<10:
        return f(start - 3,end) + f(start//3,end)
    if start%3 == 1 and start>=10:
        return f(start - 3,end) + f(start//10,end)
    if start%3 == 1 and start<10:
        return f(start - 3,end)

print(f(1250,20))