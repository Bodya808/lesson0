from threading import Thread, Lock
import threading
import random
from time import sleep


class Bank:
    def __init__(self):
        self.balance = 100
        self.lock = Lock()

    def deposit(self):
        for i in range(100):
            amount = random.randint(50, 500)

            if self.balance + amount > 500 and self.lock.locked():
                self.lock.release()

            with self.lock:
                self.balance += amount
                print(f'Пополнение: {amount}. Баланс: {self.balance}')
            sleep(0.001)

    def take(self):
        for j in range(100):
            amount = random.randint(50, 500)
            print(f'Запрос на: {amount}.')
            if amount <= self.balance:
                with self.lock:
                    self.balance -= amount
                    print(f"Снятие: {amount}. Баланс: {self.balance}")
            else:
                print("Запрос отклонён, недостаточно средств")
                self.lock.acquire()

            sleep(0.001)


bk = Bank()
th1 = threading.Thread(target=Bank.deposit, args=(bk,))
th2 = threading.Thread(target=Bank.take, args=(bk,))

th1.start()
th2.start()

th1.join()
th2.join()

print(f"Итоговый баланс: {bk.balance}")
