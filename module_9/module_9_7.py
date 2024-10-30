# Домашнее задание по теме "Декораторы"


def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if isinstance(result, bool):
            print("ERROR!")
        elif isinstance(result, int):
            print("Простое")
        else:
            print("Составное")
        return result
    return wrapper

@is_prime
def sum_three(first, second, third):
    try:
        result = first + second + third
    except TypeError:
        result = False
    return result




result = sum_three(2, 3, 4)
print(result)
print()
result = sum_three(2, 3, 7.1)
print(result)
print()
result = sum_three(2, 3, "aaa")
print(result)
print()
