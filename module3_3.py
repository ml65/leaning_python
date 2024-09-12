# Самостоятельная работа по уроку "Распаковка позиционных параметров".

# Задача "Распаковка":

def print_params(a = 1, b = 'строка', c = True):
    print (a, b, c)

print_params(1,2,3)
print_params("Один", "два")
print_params(2.01)
print_params(b = 25)
print_params(c = [1,2,3])

values_list = [4, "Пять", 6.0]
values_dict = {"a":7,"b":"Восемь","c":False}

print_params(*values_list)
print_params(**values_dict)

values_list_2=[9,"десять"]
print_params(*values_list_2, 42)