# Домашнее задание по теме "Создание функций на лету"

from contextlib import redirect_stdout
import io
from random import choice

# Задача "Функциональное разнообразие":

# Lambda-функция:

first = 'Мама мыла раму'
second = 'Рамена мало было'
result = list(map(lambda a, b: True if a == b else False , first, second))
print("================================\nLambda-функция:")
print (result)

# Замыкание:
# задачу записи объекта в файл можно решить несколькими способами:
#  * разбором объекта по ключам,
#  * сериализацией,
#  * преобразованим в json,
#  * использованием стандартного вывода с перехватом в переменную
# решил выполнить по последнему методу, т.к. подобный вывод ближе к формату в поставленной задаче

def to_str(a):
    '''
    преобразует любой объект в строку через команду print и перехват стандартного вывода
    :param a:
    :return: str
    '''
    f = io.StringIO()
    with redirect_stdout(f):
        print(a)
    return f.getvalue()

def get_advanced_writer(file_name):

    def write_everithing(*data_set):
        file = open(file_name,"a")
        for data in data_set:
            file.write(to_str(data))
        file.close()

    return write_everithing

print("\n================================\nЗамыкание:")
write = get_advanced_writer('example.txt')
write('Это строчка', ['А', 'это', 'уже', 'число', 5, 'в', 'списке'])
file = open('example.txt','r')
for str in file:
    print(str, end = '')

# Метод __call__:

class MysticBall:
    def __init__(self, *ballist):
        self.ballist = ballist

    def __call__(self):
        return choice(self.ballist)
print("\n================================\nМетод __call__:")
first_ball = MysticBall('Да', 'Нет', 'Наверное')
print(first_ball())
print(first_ball())
print(first_ball())
