# Домашнее задание по теме "Очереди для обмена данными между потоками."
from queue import Queue
from random import randint
from threading import Thread
import time
# Задача "Потоки гостей в кафе":

class Table:
    number = 0
    guest = None

    def __init__(self, number):
        self.number = number

class Guest(Thread):
    name = None

    def __init__(self, name):
        Thread.__init__(self)
        self.name = name

    def run(self):
        sleep = randint(3,10)
        time.sleep(sleep)

class Cafe:
    queue = None
    tables = []
    timer = 0
    def __init__(self, *tables):
        self.queue = Queue()
        for table in tables:
            self.tables.append(table)

    def guest_arrival(self, *guests):
        for guest in guests:
            table = self.get_free_table()
            if (table):
                table.guest = guest
                print(f"{guest.name} сел(-а) за стол номер {table.number}")
                guest.start()
            else:
                self.queue.put(guest)
                print(f"{guest.name} в очереди")

    def discuss_guests(self):
        pri = True
        while(pri):
            free = True
            for table in self.tables:
                if table.guest != None:
                    if (not table.guest.is_alive()):
                        print(f"{table.guest.name} покушал(-а) и ушёл(ушла)")
                        table.guest = None
                if table.guest == None:
                    if not self.queue.empty():
                        guest = self.queue.get()
                        table.guest = guest
                        free = False
                        print(f"{guest.name} вышел(-ла) из очереди и сел(-а) за стол номер {table.number}")
                        guest.start()
                else:
                    free = False
            if (free and self.queue.empty()):
                pri = False
            else:
                time.sleep(1)

    def get_free_table(self):
        for table in self.tables:
            if table.guest == None:
                return table
        return False

# Создание столов
tables = [Table(number) for number in range(1, 6)]
# Имена гостей
guests_names = [
    'Maria', 'Oleg', 'Vakhtang', 'Sergey', 'Darya', 'Arman',
    'Vitoria', 'Nikita', 'Galina', 'Pavel', 'Ilya', 'Alexandra'
]
# Создание гостей
guests = [Guest(name) for name in guests_names]
# Заполнение кафе столами
cafe = Cafe(*tables)
# Приём гостей
cafe.guest_arrival(*guests)
# Обслуживание гостей
cafe.discuss_guests()