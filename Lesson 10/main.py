__author__ = 'Юзов Евгений, Geekbrain'

# -*- coding: utf-8 -*-

"""
Задача 44: В ячейке ниже представлен код генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача 
перевести его в one hot вид. Сможете ли вы это сделать без get_dummies?

import random
lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI':lst})
data.head()
"""

import pandas as pd
import random
import collections


def get_one_hot(inlst: list) -> list:
    print(f'Входной список:\n {inlst}')
    for itm in collections.Counter(lst).keys():
        outlst = [True if lst[k] == itm else False for k in range(0, len(lst), 1)]
        yield outlst


if __name__ =="__main__":
    lst = ['robot'] * 5
    lst += ['human'] * 5
    lst += ['animal'] * 5
    random.shuffle(lst)
    df = pd.DataFrame(columns=list(collections.Counter(lst).keys()))
    for i, itm in enumerate(list(zip(*list(get_one_hot(lst))))):
        df.loc[len(df)] = list(itm)
    print(f'Выходной DataFrame без использования get_dummies():\n {df}')

