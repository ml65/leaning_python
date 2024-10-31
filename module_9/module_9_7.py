# Домашнее задание по теме "Декораторы"


def is_prime(func):
    def wrapper(*args):
        result = func(*args)
        if (result):
            is_prime = True

            if result <= 1:
                is_prime = False
            if result == 2:
                is_prime = True
            if result % 2 == 0:
                is_prime = False
            for i in range(3, int(result ** 0.5) + 1, 2):
                if result % i == 0:
                    is_prime = False
            if is_prime:
                print("Простое")
            else:
                print("Составное")

        return result
    return wrapper

@is_prime
def sum_three(first:int, second:int, third:int):
    try:
        result = int(first) + int(second) + int(third)
    except TypeError:
        print("ERROR!")
        result = ""
    except ValueError:
        print("ERROR!!!")
        result = ""
    return result




result = sum_three(12, 3, 4)
print(result)
print()
result = sum_three(2, 3, 7.1)
print(result)
print()
result = sum_three(2, 3, "aaa")
print(result)
print()
