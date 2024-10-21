# Домашнее задание по теме "Введение в функциональное программирование"

# Задача "Вызов разом":

import types

def apply_all_func(int_list, *functions):
    result = {}
    for func in functions:
        try:
            result[func.__name__] = func(int_list)
        except:
            print("Что-то пошло не так:", int_list, func)

    return result

print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
print(apply_all_func([6, 20, 15, 9], 'len', sum, sorted))
print(apply_all_func(123, 'len', sum, sorted))