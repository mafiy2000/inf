from itertools import permutations, product

def f (x,y,w,z): #писываем исходную функцию
    return ((x <= y) or (z <= w)) and ((z != y) <= (w != x))

for c in product([0,1], repeat = 4): #комбинации 0 и 1 по числу пустых клеток
    table = [(c[0],1,0,c[1]), (0,1,0,1), (c[2],1,0,c[3])] #формирование таблиц
    if len(table) == len(set(table)):  #проверка на неповторяемость строк
        for p in permutations('xywz'): #перестановки переменных
            if [f(**dict(zip(p,row))) for row in table] == [0,0,0]:
                print('answer', p)