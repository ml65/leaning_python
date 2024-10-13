# Самостоятельная работа по уроку "Рекурсия"

# Задача "Рекурсивное умножение цифр":

def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    if (len(str_number) > 1):
        return first * get_multiplied_digits(int(str_number[1:]))
    else:
        if first > 0:
            return first
        else:
            return 1

result = get_multiplied_digits(420)
print (result)
