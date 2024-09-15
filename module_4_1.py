# Домашняя работа по уроку "Модули и пакеты"

# Задача "А как делить?":
# module_4_1.py
# fake_math.py
# true_math.py

from fake_math import divide as fake_divide
from true_math import divide as true_divide

result1 = fake_divide(69,3)
result2 = fake_divide(3,0)
result3 = true_divide(49,7)
result4 = true_divide(15,0)
result5 = true_divide('69', 3)

print(result1)
print(result2)
print(result3)
print(result4)
print(result5)


