__author__ = 'Юзов Евгений, Geekbrain'

# -*- coding: utf-8 -*-

"""
Задача 1:
Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.
Найдите количество и выведите его.
list_1 = [1, 2, 3, 4, 5]
k = 3
#1

Задача 2:
Требуется найти в массиве list_1 самый близкий по величине элемент к заданному числу k и вывести его.
list_1 = [1, 2, 3, 4, 5]
k = 6
# 5

Задача 3:
В настольной игре Скрабл (Scrabble) каждая буква имеет определенную ценность.
В случае с английским алфавитом очки распределяются так:
    A, E, I, O, U, L, N, S, T, R – 1 очко;
    D, G – 2 очка;
    B, C, M, P – 3 очка;
    F, H, V, W, Y – 4 очка;
    K – 5 очков;
    J, X – 8 очков;
    Q, Z – 10 очков.
А русские буквы оцениваются так:
    А, В, Е, И, Н, О, Р, С, Т – 1 очко;
    Д, К, Л, М, П, У – 2 очка;
    Б, Г, Ё, Ь, Я – 3 очка;
    Й, Ы – 4 очка;
    Ж, З, Х, Ц, Ч – 5 очков;
    Ш, Э, Ю – 8 очков;
    Ф, Щ, Ъ – 10 очков.
Напишите программу, которая вычисляет стоимость введенного пользователем слова k и выводит его. Будем считать, 
что на вход подается только одно слово, которое содержит либо только английские, либо только русские буквы.
k = 'ноутбук'
# 12
"""


def count(list_1: list, num: int) -> int:
    return len(list(filter(lambda x: x == num, list_1)))


"""точный способ!"""


def closer(list_1: list, num: int) -> list:
    lst = list(map(lambda x: abs(num - x), list_1))
    mi = min(lst)
    return [i for i in range(0, len(lst)) if lst[i] == mi]


"""не точный способ!"""


def closer1(list_1: list, num: int) -> list:
    mi = min(list_1, key=lambda x: abs(num - x))
    return [i for i in range(0, len(list_1)) if list_1[i] == mi]


def getpoint(value) -> int:
    points: dict[int, list[str]] = {1: ['A', 'E', 'I', 'O', 'U', 'L', 'N', 'S', 'T', 'R'],
                                    2: ['D', 'G'],
                                    3: ['B', 'C', 'M', 'P'],
                                    4: ['F', 'H', 'V', 'W', 'Y'],
                                    5: ['K'],
                                    8: ['J', 'X'],
                                    10: ['Q', 'Z']}
    for point, lst in points.items():
        for i in lst:
            if i == value:
                return point


def scrabble(value: list) -> int:
    summa = 0
    for itm in value:
        summa = summa + getpoint(itm)
    return summa


if __name__ == '__main__':
    print(count([1, 2, 3, 4, 5, 3, 4, 5, 6, 7, 3, 2, 2, 4, 5, 7, 6, 4, 1, 3, 3, 34, 5, 6, 7, 0, 4, 0, 3, 3, 5, 6], 3))
    print(closer([1, 2, 3, 4, 5, 8, 3, 5, 6, 8, 4, 2, 10], 7))
    print(closer1([1, 2, 3, 4, 5, 8, 3, 5, 6, 8, 4, 2, 10], 7))
    print(closer([1, 2, 3, 4, 5, 7, 8, 3, 5, 6, 8, 4, 2, 10], 7))
    print(closer1([1, 2, 3, 4, 5, 7, 8, 3, 5, 6, 8, 4, 2, 10], 7))
    #4+1+1+4+1+1+2
    print(scrabble('FORWARD'))
    print(scrabble("PYTHONIST"))
