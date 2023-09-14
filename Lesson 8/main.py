"""
Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, номер
телефона - данные, которые должны находиться в файле.
1. Программа должна выводить данные
2. Программа должна сохранять данные в текстовом файле
3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию
человека)
4. Использование функций. Ваша программа не должна быть линейной

Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести
имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных
"""
from typing import TextIO

import pandas as pd


# import csv

class Person:
    __type = "Person"
    __default = "Undefined"

    @staticmethod
    def object_type():
        print(Person.__type)

    def __init__(self, first_name=__default, second_name=__default, desc=__default) -> None:
        self.first_name = first_name  # Имя человека
        self.second_name = second_name  # Фамилия человека
        self.description = desc  # Описание человека

    def __str__(self) -> str:
        return f"Имя: {self.first_name}, Фамилия: {self.second_name}, Описание: {self.description}"


class Phonebook:
    __type = "Phonebook"

    @staticmethod
    def object_type() -> None:
        print(Phonebook.__type)

    @classmethod
    def __create_csv(cls, filename: str) -> TextIO: # Создаём нужный текстовый файл
        try:
            columns = ['Имя', 'Фамилия', 'Описание', "Телефон"]
            df = pd.DataFrame(columns=columns)
            df.to_csv(filename)
            return open(filename, "a")
        except FileExistsError:
            return open(filename, "a")

    def __init__(self, filename):
        self.__file = Phonebook.__create_csv(filename)

    @property
    def file(self):
        return self.__file

    def create(self, person: Person, phone_number: str):  # Создаёт запись
        print(f'{person}, Телефонный номер: {phone_number}')

    def find(self):  # Ищет записи
        pass

    def update(self):  # Обновляет запись
        pass

    def delete(self):  # Стирает запись
        pass


if __name__ == "__main__":
    p1 = Person(first_name="Вася", second_name="Пупкин", desc="Тестовый пользователь")
    print(p1)
    p2 = Person(first_name="Женя")
    p2.second_name = "Юзов"
    print(p2)
    ph = Phonebook("textfile.csv")
    print(ph.file.name)
    ph.create(p1, '+79173961424')
