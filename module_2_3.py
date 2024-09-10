# Домашняя работа по уроку "Стиль кода часть II. Цикл While."

my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list) and my_list[i] >= 0:
    if 0 < my_list[i]:
        print (my_list[i])
    i += 1
# Вариант с использованием операторов break и continue
print ("v2.0")
i = 0
while i < len(my_list):
    if my_list[i] > 0:
        print (my_list[i])
    elif my_list[i] < 0:
        break
    i += 1

