__author__ = 'Юзов Евгений, Geekbrain'

import string
# from functools import reduce

# -*- coding: utf-8 -*-

"""
Задача 34: Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку
разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам
стоит написать программу. Винни-Пух считает, что ритм есть, если число слогов (т.е. число
гласных букв) в каждой фразе стихотворения одинаковое. Фраза может состоять из одного
слова, если во фразе несколько слов, то они разделяются дефисами. Фразы отделяются друг
от друга пробелами. Стихотворение Винни-Пух вбивает в программу с клавиатуры. В ответе
напишите “Парам пам-пам”, если с ритмом все в порядке и “Пам парам”, если с ритмом все не
в порядке
Ввод:
пара-ра-рам рам-пам-папам па-ра-па-дам
Вывод: 
Парам пам-пам

Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
ровно два аргумента, как, например, у операции умножения.
Ввод:
print_operation_table(lambda x, y: x * y)
Вывод:
1 2 3 4 5 6
2 4 6 8 10 12
3 6 9 12 15 18
4 8 12 16 20 24
5 10 15 20 25 30
6 12 18 24 30 36
"""


def display(in_func):
    def out_function(*args):
        print(dict(enumerate(in_func(*args))))
    return out_function


def count_vowels(txt: list) -> int:
    volwes = set('аоэеиыуёюя')
    return sum([1 for a in txt if a in volwes])


def rithm(txt: string) -> None:
    a = txt.lower().split(" ")
    itm = list(map(lambda x: count_vowels(x), a))
    if max(itm) == min(itm):
        print('Парам пам-пам')
    else:
        print('Пам парам')


@display
def rithm_count(txt: string) -> map:
    a = txt.lower().split(" ")
    return map(lambda x: count_vowels(x), a)


def print_operation_table(operation, **kwargs) -> None:
    num_rows = kwargs.get('num_rows', 6)
    num_columns = kwargs.get('num_columns', 6)
    for row in [[operation(row, column) for column in range(1, num_columns + 1)] for row in range(1, num_rows + 1)]:
        print(*row, sep=" ")


if __name__ == '__main__':
    rithm_count("пара-ра-рам рам-пам-папам па-ра-па-дам")
    print('\n' + '=' * 25 + '\n')
    rithm("пара-ра-рам рам-пам-папам па-ра-па-дам")
    rithm("пара-ра-рам рам-пам-папам па-ра-па-дам ооооооооо-вввввв")
    print('\n' + '=' * 30 + '\n')
    print_operation_table(lambda x, y: x * y)
    print('\n' + '=' * 30 + '\n')
    print_operation_table(lambda x, y: x * y, num_rows=10, num_columns=10)
    print('\n' + '=' * 30 + '\n')
    print_operation_table(lambda x, y: x * y, num_rows=100, num_columns=100)
