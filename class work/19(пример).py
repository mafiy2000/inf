# функция которая проверяет можно ли выйграть за m ходов
def f(s, c, m): # s - кол-во камней в кучке, c - кол-ов ходов выполненых во время игры, m - порог ходов, в которым мы себя ограничиваем
    # если игра окончена, то кол-во ходов ддолжно иметь ту же четность. что и m
    if s>=30: return c%2 == m%2
    # если игра не закончилась за m ходов, то забиваем
    if c == m: return 0

    # тож самое, но без списка,  all и any
    # if (c + 1) % 2 == m % 2: return f(s+2,c+1,m) or f(s+2,c+1,m) or f(s*2,c+1,m)
    # else: return f(s+2,c+1,m) and f(s+2,c+1,m) and f(s*2,c+1,m)

    # смотрим следующие ходы
    h = [f(s+2,c+1,m), f(s+2,c+1,m),f(s*2,c+1,m)]
    # Если ход целевого игрока, то достаточно победы одного из вариантов
    # иначе победа должна быть во всех вариантах
    return any(h) if (c+1)%2 == m%2 else all(h)
#ниже написано для условий заданий
for s in range(1,30):
    for m in range(1,5):
        if f(s,0,m)==1:
            print(s,m)
            # если нашлась выйгрышная стратегия, то дальше не копаем
            break

