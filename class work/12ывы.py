for n in range(2,1000):
    s = '3' + ((n>3) * '7')
    while '37' in s or '577' in s or '777' in s:
        if '37' in s:
            s == s.replace('37', '7', )
        if '577' in s:
            s == s.replace('577', '73', )
        if '777' in s:
            s == s.replace('777', '5', )
            break
print(s)
