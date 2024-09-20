from threading import Thread
from datetime import datetime
from time import sleep


class Knight(Thread):
    def __init__(self, name: str, power: int):
        super().__init__()
        self.name = name
        self.power = power
        self.enemy = 100
        self.day = 0


    def run(self):
        print(f'{self.name}, на нас напали!')
        while self.enemy != 0:
            sleep(1)
            self.day += 1
            self.enemy -= self.power
            print(f'{self.name} сражается {self.day}, осталось {self.enemy} воинов.')
            if self.enemy == 0:
                print(f'{self.name} одержал победу спустя {self.day} дней(дня)!')
                break



first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

first_knight.start()
second_knight.start()
first_knight.join()
second_knight.join()

print('Все битвы закончились!')


