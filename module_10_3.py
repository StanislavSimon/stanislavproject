import threading
import random
import time

class Bank:
    def __init__(self):
        self.balance = 0
        self.lock = threading.Lock()


    def deposit(self):
        for _ in range(100):
            payment = random.randint(50, 500)
            self.lock.acquire()
            if self.balance >= 500 and self.lock.locked():
                self.lock.release()
            self.balance += payment
            print(f"Пополнение: {payment}. Баланс: {self.balance}")
            time.sleep(0.001)

    def take(self):
        for _ in range(100):
            removal = random.randint(50, 500)
            print(f'Запрос на: {removal}')
            if removal <= self.balance:
                self.balance -= removal
                print(f'Снятие: {removal}. Баланс: {self.balance}')
            else:
                print(f"Запрос отклонен, недостатосно средств")
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