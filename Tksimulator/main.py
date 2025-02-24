"""
import random


class Dog:
    def __init__(self, name, hunger, joy, day = 0):
        self.name = name
        self.day = day
        self.hunger = hunger
        self.joy = joy
        self.alive = True

    def to_eat(self):
        print(f"Day:{self.day}")
        print("Time to eat!")
        self.hunger += 0.5
        self.joy += 0.4
        self.end_of_day()

    def to_play(self):
        print(f"Day:{self.day}")
        print("Time to play!")
        self.hunger -= 0.6
        self.joy += 0.3
        self.end_of_day()

    def to_nothing(self):
        print(f"Day:{self.day}")
        print("Nothing happened!")
        self.hunger -= 0.6
        self.joy -= 0.5
        self.end_of_day()

    def end_of_day(self):
        print(f"Hunger: {round(self.hunger, 2)}")
        print(f"Joy: {round(self.joy, 2)}")
        self.day += 1

    def is_alive(self):
        if self.hunger < 6:
            print("Death")
            self.alive = False
        elif self.joy < 10:
            print("Sadness")
            self.alive = False
        elif self.joy > 60:
            print("Victory!")
            self.alive = False

    def live(self):
        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_play()
        elif live_cube == 2:
            self.to_nothing()
        elif live_cube == 3:
            self.to_eat()


print("----------------------------- Dog simulator -----------------------------")
a = input("Choose name:")
b = int(input("Choose days:"))
c = int(input("Choose hunger:"))
d = int(input("Choose joy:"))

player = Dog(a,c,d)
while player.day < b:
    player.live()

"""
"""
from colorama import Fore, Back, Style


class Text:
    color = True


a = Text()
print(Fore.BLUE + 'Some text')
b = print(Back.YELLOW + 'Textt')
c = print(Style.RESET_ALL)



print("a is in list:",isinstance(a, list))
print("Color:",hasattr(a, 'color'))

print("Id:",id(a))
"""