"""
import random

print("-------------------------- Симулятор студента --------------------------")

class Student:
    def __init__(self, name):
        self.name = name
        self.day = 1
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print(f"Day: {self.day}")
        print("Час вчитись!")
        self.progress += 0.12
        self.gladness -= 0.1
        self.end_of_day()

    def to_chill(self):
        print(f"Day: {self.day}")
        print("Відпочинок!")
        self.progress -= 0.06
        self.gladness += 0.06
        self.end_of_day()

    def to_sleep(self):
        print(f"Day: {self.day}")
        print("Час спати!")
        self.gladness += 0.08
        self.end_of_day()

    def is_alive(self):
        if(self.progress == 0):
            print("Вигнали!")
            self.alive = False
        elif(self.gladness == 0):
            print("Депресія!")
            self.alive = False
        elif(self.progress > 5):
            print("Здано іспит екстерном!")
            self.alive = False

    def end_of_day(self):
        print(f"Gladness: {round(self.gladness, 2)}")
        print(f"Progress: {round(self.progress, 2)}")
        self.day += 1

    def live(self):
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_chill()
        elif live_cube == 3:
            self.to_sleep()

student = Student("John")

while student.day < 365:
    student.live()
    student.is_alive()
    if student.alive == False:
        break
"""
#import inspect


import random

class Dog:
    def __init__(self, name):
        self.name = name
        self.day = 0
        self.hunger = 40
        self.joy = 40
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
        elif self.joy > 65:
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

class Human:
    def __init__(self, name):
        self.name = name
        self.day = 1
        self.exhaustion = 5
        self.joy = 40
        self.alive = True

    def to_play(self):
        print(f"Day:{self.day}")
        print("Time to play with dog!")
        self.exhaustion += 0.5
        self.joy += 0.4
        self.end_of_day()
    def to_sleep(self):
        print(f"Day:{self.day}")
        print("Time to sleep!")
        self.exhaustion -= 0.4
        self.joy += 0.4
        self.end_of_day()
    def to_feed(self):
        print(f"Day:{self.day}")
        print("Time to feed dog!")
        self.exhaustion += 0.5
        self.joy += 0.3
        self.end_of_day()

    def end_of_day(self):
        print(f"Exhaustion: {round(self.exhaustion, 2)}")
        print(f"Joy: {round(self.joy, 2)}")
        self.day += 1

    def is_alive(self):
        if self.exhaustion > 60:
            print("Exhaustion")
            self.alive = False
        elif self.joy < 7:
            print("Sadness")
            self.alive = False
        elif self.joy > 65:
            print("Victory!")
            self.alive = False

    def live(self):
        live_cube = random.randint(1, 3)

        if live_cube == 1:
            self.to_play()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_feed()

print("----------------------- Life simulator ----------------------- ")

a = input("Choose race(Human/Dog):")
b = input("Choose name:")
c = int(input("Choose days of live(1/365):"))

if a == "Human" or "human":
    human = Human(name=b)
    while human.day < c:
        human.live()
        human.is_alive()
        if human.day == c:
            break
        elif human.alive == False:
            break
if a == "Dog" or "dog":
    dog = Dog(name=b)
    while dog.day < c:
        dog.live()
        dog.is_alive()
        if dog.day == c:
            break
        elif dog.alive == False:
            break


#import requests

"""
def first_func():
    pass
class Human:
    pass

rq = requests
first_f = first_func
name = Human

#print(requests.__name__)
#print(rq.__name__)
#print(first_func.__name__)
#print(first_f.__name__)
#print(Human.__name__)
#print(name.__name__)

print(__name__)
"""

#list1 = []
#for method in dir(list1):
#    print(method)

#list1 = []
#for method in dir():
 #   print(method)

# data = "string"
# print(hasattr(data, "reverse"))
# print(hasattr(data, "index"))
#
# print(getattr(data, "startswith"))
# print(getattr(data, "startswith",None))
# print(getattr(data, "reverse",None))

#data = "string"
#def first_func():
#    pass
#print(callable(data))
#
#print(callable(first_func))

#data = "string"

#class First_class:
   # pass

#class Second_class:
   # pass

#print(issubclass(First_class, Second_class))
#print(issubclass(Second_class, First_class))

#data = "string"
#class First_class:
#    pass
#class Second_class(First_class):
#    pass
#
#obj_from_class2 = Second_class()
#
#print(isinstance(obj_from_class2,First_class))
#print(isinstance(obj_from_class2,Second_class))

'''----------------------------------------------'''

'''
import inspect

print(inspect.ismodule(requests)) # перевіряє чи об'єкт є модулем
print(inspect.isclass(requests)) # перевіряє чи є класом
print(inspect.isfunction(requests)) # перевіряє чи є функцією

print(inspect.getmodule(requests.get)) # повертає назву модуля в якому створено об'єкт

print(inspect.getmodule(list)) # 
'''

"""
class Human:
    def __init__(self, age, height = 170, name = "John"):
        self.age = age
        self.height = height
        self.name = name
sig = inspect.signature(Human)
for parameter in sig.parameters.values():
    print(parameter.name, parameter.default)
"""

import sys

#print(sys.executable)
#print(sys.version)

#print(sys.platform)

#print(sys.argv)

#for module_name, module_path in sys.modules.items():
#    print(module_name, module_path)

#for _ in dir(__builtins__):
#    print(_)

