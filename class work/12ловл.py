#хотя бы по 100 единиц и двоек
#Сумма цифр не зависит от их порядка!
#Сумма уменьшится на один

def p(x):
    return x>1 and all(x%i!=0 for i in range(2, int(x**0.5)+1))

for n in range(100, 150):
    if p(3*n-1):
        print(n)