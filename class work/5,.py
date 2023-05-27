def f(x):
    b = bin(x)[2:]
    ch = len([d for d in str(x) if d in '02468'])
    nch = len(str(x)) - ch
    if ch>nch: b = b + '1'
    if nch>ch: b = b + '0'
    if ch == nch: b = b + str(x%2)
    return int(b,2)

def g(x):
    return f(f(f(x))) # повторяем первую функцию 3 раза
# Тк мы дописываем 3 двоичных числа то мы удваиваем число в 8 раз
print(g(15431))
print(g(123456790))
print(123456790 - 15431 + 4)