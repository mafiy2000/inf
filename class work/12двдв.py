for n in range(2, 100):
    s = '3' + n * '5'
    while '25' in s or '355' in s or '555' in s:
        s = s.replace('25', '3')
        break
        if '355' in s:
            s = s.replace('355', '52')
            break
        if '555' in s:
            s = s.replace('553', '23')
            break