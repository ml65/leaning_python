# Домашняя работа по уроку "Условная конструкция. Операторы if, elif, else."
#
# Решение согласно увловиям задачи без пользовательского интерфейса
#
# a = input()
# b = input()
# c = input()
#
# if (a == b and b == c):
#     print (3)
# elif (a==b or b==c or a==c):
#     print (2)
# else:
#     print (0)

print ("Введите три числа")
a = input("Первое число: ")
b = input("Второе число: ")
c = input("Третье число: ")

if (a == b and b == c):
    print (3)
elif (a==b or b==c or a==c):
    print (2)
else:
    print ("Результат по условию задачи:",0)
