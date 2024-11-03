# Домашнее задание по теме "Потоки на классах
#
import threading
import time

# Задача "За честь и отвагу!":


class Knight(threading.Thread):
    def __init__(self, name, power):
        threading.Thread.__init__(self)
        self.name = name
        self.power = power
        self.enemy = 100

    def run(self):
        print(f"{self.name} на нас напали!")
        day = 0
        while self.enemy > 0:
            self.enemy += -self.power
            day += 1
            time.sleep(1)
            print(f"{self.name}, сражается {day} день(дня)")
        print(f"{self.name}, одержал победу спустя {day} дней(дня)!")

# Создание класса
first_knight = Knight("Sir Lancelot", 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()
print("Все битвы закончились!")


# Запуск потоков и остановка текущего
# Вывод строки об окончании сражения
