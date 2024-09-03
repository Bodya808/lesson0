import time
from threading import Thread
from time import sleep


class Knight(Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        enemies = 100
        days_count = 0
        print(f"{self.name}, на нас напали!")
        while enemies > 0:
            time.sleep(1)
            days_count += 1
            enemies -= self.power
            if enemies > 0:
                print(f'{self.name} сражается {days_count} день(дня)..., '
                      f'осталось {enemies} воинов.')
            else:
                print(f'{self.name} одержал победу спустя {days_count} дней(дня)!')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)
first_knight.start()
second_knight.start()

first_knight.join()
second_knight.join()

print('Все битвы закончились!')
