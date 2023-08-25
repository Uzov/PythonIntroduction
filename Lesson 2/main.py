__author__ = 'Юзов Евгений, Geekbrain'

# -*- coding: utf-8 -*-

"""
Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. 
Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх 
одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть

Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. 
Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. 
Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.
"""


def mincoins(coins: tuple) -> None:
    count = 0
    for coin in coins:
        if coin == 1: count += 1
    print(count) if count <= len(coins) / 2 else print(len(coins) - count)


def guess(gSum: int, gProd:int) -> tuple[int, int]:
    for i in range(1, int(gProd / 2), 1):
        if i == int(gProd / 2) - 1:
            return -1, -1
        if (gSum == gProd / i + i):
            return i, gSum - i


def powertwo(N: int) -> list:
    p = 1
    while p <= N:
        yield p
        p *= 2


if __name__ == '__main__':
    mincoins((1, 1, 0, 0, 0, 0, 0, 1))
    mincoins((1, 1, 0, 1, 1, 0, 0, 1))
    mincoins((1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 1, 0, 0, 1))
    print(list(powertwo(10)))
    print(list(powertwo(100)))
    print(list(powertwo(512)))
    print(tuple(guess(7, 10)))  # 2 и 5
    print(tuple(guess(1284, 396288)))  # 768 и 516
    print(tuple(guess(10, 25)))  # 5 и 5
    print(tuple(guess(10, 26)))  # ? и ?
