# -*- coding: utf-8 -*-


def Zpow(a, p, m):
    """
    Функция возведения в степень по модулю
    принимает 3 аргумента
    a - сам математический аргумент, возводимое число
    p - степень
    m - модуль
    """
    result = 1
    while p > 2: # когда степень сократится до квадрата и меньше - завершаем
        if p % 2 == 0: # если степень кратна 2
            a = (a ** 2) % m
            p = p // 2 # целочисленное деление (на всякий)
        else:
            result = (result * a) % m
            p = p - 1
    a = (a ** p) % m
    result = (result * a) % m
    return result


if __name__ == '__main__':
    # реализуем интерфейс для теста:
    __exit = False
    while not __exit:
        a = input("Введите аргумент, число a:")
        p = input("Введите степень, число p:")
        m = input("Введите модуль, число m:")
        try:
            a = int(a)
            p = int(p)
            m = int(m)
        except ValueError:
            print("ERROR: Вввести необходимо целые числа")
            continue
        print("Результат функции ----->>> ", Zpow(a, p, m))
        req = input("Вы ходите выйти? Y/N: ")
        if req != 'N':
            __exit = True
