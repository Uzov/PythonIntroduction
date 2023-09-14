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

import pandas as pd

def display(in_func): # Декоратор для печати DataFrame
    def out_function(*args):
        print(dict(enumerate(in_func(*args))))
    return out_function

class Person:
    __type = "Person"
    __default = "Undefined"

    @staticmethod
    def object_type() -> None:
        print(Person.__type)

    def __init__(self, second_name=__default, first_name=__default, surname=__default, desc=__default) -> None:
        self.first_name = first_name  # Имя человека
        self.second_name = second_name  # Фамилия человека
        self.surname = surname  # Отчество
        self.description = desc  # Описание человека

    def __str__(self) -> str:
        return f"Фамилия: {self.second_name}, Имя: {self.first_name}, Отчество: {self.surname}, " \
               f"Описание: {self.description}"


class Phonebook:
    __type = "Phonebook"

    @staticmethod
    def object_type() -> None:
        print(Phonebook.__type)

    @classmethod
    def __create_csv(cls, filename: str) -> None:  # Создаём нужный текстовый файл
        try:
            columns = ['second_name', 'first_name', 'surname', 'description', 'phone_number']
            df = pd.DataFrame(columns=columns)
            df.to_csv(filename, sep=";", mode='x')
        except FileExistsError:
            pass

    def __init__(self, filename):
        Phonebook.__create_csv(filename)
        self.__filename = filename

    @property
    def file(self) -> str: # Узнать имя файла текущей телефонной книги
        return self.__filename

    def add(self, person: Person, phone_number: str) -> None:  # Добавляет запись в конец файла
        df = pd.DataFrame({'second_name': [person.second_name, ],
                           'first_name': [person.first_name, ],
                           'surname': [person.surname, ],
                           'description': [person.description, ],
                           'phone_number': [phone_number, ]})
        try:
            df.to_csv(self.__filename, mode='a', index=False, header=False, sep=";")
            print(f'Запись {person} с телефонным номером: {phone_number} успешно добавлена!')
        except Exception as error:
            print(f'Запись {person} с телефонным номером: {phone_number} не добавлена!')
            print(f'Произошла следующая ошибка: {error}!')

    def read(self): # Читает и выводит весь файл
        df = pd.read_csv(self.__filename, delimiter=';',
                         names=["Фамилия:", "Имя:", "Отчество:", "Описание:", "Телефон:"])
        print(f'Найдено {len(df)} записей:\n{df}')

    def find(self, display=True, *args):  # Ищет записи, если число критериев больше нуля
        if len(args) == 0:
            print(f'Записи не могут быть найдены! Введите хотя бы один аргумент!')
            return
        df = pd.read_csv(self.__filename, delimiter=';',
                         names=["Фамилия:", "Имя:", "Отчество:", "Описание:", "Телефон:"])
        lst = [*args]
        for col in lst:
            df = df[df.isin([col, ]).any(axis=1)]
        if display:
            print(f'Найдено {len(df)} записей:\n{df}')
        else:
            return df

    def update(self, *args):  # Обновляет запись
        df = self.find(False, *args)
        if len(df) == 0:
            print(f'Запись для обновления не найдена, нечего обновлять!')
        elif len(df) > 1:
            print(f'Найдено {len(df)} записей:\n{df}')
            input("Выберите id записи для обновления: ")

    def delete(self, *args):  # Стирает запись
        df = self.find(False, *args)
        if len(df) == 0:
            print(f'Запись для удаления не найдена, нечего удалять!')
        elif len(df) > 1:
            print(f'Найдено {len(df)} записей:\n{df}')
            lst = [int(x) for x in input("Введите через пробел id записей для удаления: ").split()]
        df = pd.read_csv(self.__filename, delimiter=';')
        df = df.drop(labels=lst, axis=0)
        print(df)



if __name__ == "__main__": # Проверка
    p1 = Person(first_name="Вася", second_name="Пупкин", desc="Тестовый пользователь")
    #print(p1)
    #p2 = Person(first_name="Женя")
    #p2.second_name = "Юзов"
    #print(p2)
    ph = Phonebook("textfile.csv")
    #ph.add(p1, '+7 916 329-55-16')
    #ph.find(True, "Людмила", "Игоревна")
    #ph.find(False, "+7 499 586-05-91")
    #ph.read()
    #ph.update("Людмила", "Игоревна")
    #ph.delete("Людмила", "Игоревна")
    ph.delete("Вася")