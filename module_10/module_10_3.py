# Домашнее задание по теме "Блокировки и обработка ошибок"

# Задача "Банковские операции":

import threading
from random import randint
import time

class Bank:
    balance = 0
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()

    def deposit(self):
        for t in range(1,100):
            sum = randint(50,500)
            if self.balance > 500 and self.lock.locked():
                self.lock.release()
            self.balance += sum
            print(f"Пополнение: {sum}. Балланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for t in range(1,100):
            sum = randint(50,500)
            print(f"Запрос на {sum}")
            if sum <= self.balance:
                self.balance -= sum
                print(f"Снятие {sum}. Балланс: {self.balance}")
            else:
                print(f"Запрос отклонен, недостаточно средств.")
                self.lock.acquire()
            time.sleep(0.001)

bk = Bank()

# Т.к. методы принимают self, в потоки нужно передать сам объект класса Bank
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()
th1.join()
th2.join()

print(f'Итоговый баланс: {bk.balance}')