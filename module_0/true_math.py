# Домашняя работа по уроку "Модули и пакеты"

# Задача "А как делить?":
# module_4_1.py
# fake_math.py
# true_math.py

# Бесконечность
from math import inf

def divide (a, b):
    '''
    :param a:
    :param b:
    :return: float | str
    '''
    if (validate(a) and validate(b)):
        if (b != 0):
            return a / b
        else:
            return inf

    else:
        # исключение мы пока не изучили
        return 'Ошибка: оба параметра должны быть числами'

def validate(par):
    if isinstance(par, int) or isinstance(par, float):
        return True

    return False

