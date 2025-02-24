"""
class Human:
    height = 170

class Student(Human):
    pass
class Worker(Human):
    pass

Nick = Student()
Anna = Worker()
print(Nick.height)
print(Anna.height)
"""

"""
class Human:
    height = 170
    progress_work = 99
class Student(Human):
    progress_work = 0
class Worker(Human):
    progress_work = 90

Nick = Student()
Anna = Worker()
print(Nick.height, Nick.progress_work)
print(Anna.height, Anna.progress_work)
"""

"""
class Grandparent:
    height = 170
    progress = 100
    age = 26

class Parent(Grandparent):
    age = 30

class Child(Parent):
    height = 150
    def __init__(self):
        print(self.height)
        print(self.progress)
        print(self.age)

Nick = Child()
"""

"""----------------  super() ----------------"""

"""
class Hello:
    def __init__(self):
        print("Hello")


class Hello_World(Hello):
    def __init__(self):
        super().__init__()
        print("World")

helloworld = Hello_World()
"""

"""
class Class1:
    var = 20

    def __init__(self):
        self.var = 10

class Class2(Class1):
    def __init__(self):
        print(self.var)
        super().__init__()
        print(self.var)
        print(super().var)

hello = Class2()
"""

"""----------------Множини успадкування----------------"""
"""----------------Синтаксис:----------------"""

"""
class Class1:
    методи-та-атрибути
class Class2:
    методи-та-атрибути
......
class Class3(Class1, Class2):
    методи - та - атрибути
"""

"""
class Computer:
    def __init__(self):
        super().__init__()
        self.memory = 128

class Display:
    def __init__(self):
        super().__init__()
        self.quality = "4k"

class Smartphone(Computer,Display):
    def print_info(self):
        print(self.memory)
        print(self.quality)



iphone = Smartphone()
iphone.print_info()
"""

"""-------------------------   *args **kwargs  -----------------------"""

"""
def printFunc(a, b , c = None):
    print("This is a:",a)
    print("This is b:",b)
    print("This is c:",c)
printFunc(1,2)
"""

"""
def printFunc(a = None, b = None , c = None):
    print("This is a:",a)
    print("This is b:",b)
    print("This is c:",c)
printFunc(c=3, a=1)
"""

"""
a = [1, 2, 3]
b = [*a, 4, 5, 6]
print(b)
"""

"""
def printStudent(Student, *scores):
    print(f"Student name:{Student}")
    for score in scores:
        print(score)

printStudent("John",100,95,45,30,56)
"""

"""
def printPetNames(owner, **animals):
    print(f"Owner name: {owner}")
    for animal, name in animals.items():
        print(f"{animal}:{name}")

printPetNames("John", Dog = "Bobik",Fish = ["Lory", "Clown", "Nemo"], Turtle = "Leonardo")
"""
"""------------------------------------------------------------------------------------------------------"""

"""
class Computer:
    def __init__(self, model, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.model = model
        self.memory = 128

class Display:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.image = "8k"

class Smartphone(Display, Computer):
    def print_info(self):
        print(self.model)
        print(self.image)
        print(self.memory)

iphone = Smartphone(model = "13ProMax")
iphone.print_info()
"""

"""--------------------------Винятки(Помилки)--------------------------"""

# синтаксис обробки винятку(помилки):

"""
try:
    #код з можливою помилкою
except:
    #код що виконується у разі помилики
"""

"""
try:
    print("start code")
    print(error)
    print("Not error")
except:
    print("ERROR!!!")


print("code after error")
"""

"""
try:
    print("start code")
    print(10/0)
    print("No errors")
except NameError:
    print("Name ERORR!!")
except ZeroDivisionError:
    print("ZERO DIVISION ERROR!!!")

print("code after error")
"""

"""
try:
    print("start code")
    print(10/0)
    print("No errors")
except(NameError, ZeroDivisionError):
    print("ZERO DIVISION ERROR!!!")

print("Code after error")
"""

"""
try:
    print("start code")
    print(10/0)
    print("No errors")
except(NameError, ZeroDivisionError) as error:
    print(error)


print("Code after error")
"""

"""
try:
    print("start code")
    print(10/2)
    print("No errors")
except(NameError, ZeroDivisionError) as error:
    print(error)
else:
    print("No errors")

print("Code after error")
"""

"""
try:
    print("start code")
    print(10/2)
    print("No errors")
except(NameError, ZeroDivisionError) as error:
    print(error)
else:
    print("No errors")
finally:
    print("Final code")

print("Code after error")
"""

"""
import warnings

def checker(var_1):
    if type(var_1) != str:
        raise TypeError(f"We cant work with type{type(var_1)}", f"We need <class 'str'>")
    else:
        return var_1

var1 = "nigga"
print(checker(var1))
"""

"""---------------------------------------- Ітератори ----------------------------------------"""

"""
my_list = [1, 2, 3]

iterator = iter(my_list)
#print(iterator)

print(next(iterator))
print(next(iterator))
print(next(iterator))
"""

"""
list = [1, 2, 3]

iterator = iter(list)
for elements in iterator:
    print(elements)
"""

"""----------------------------------------Ітеровані об'єкти ----------------------------------------"""

"""
class Counter:
    def __init__(self, max_num):
        self.i = 0
        self.max_num = max_num
    def __iter__(self):
        self.i = 0
        return self
    def __next__(self):
        self.i += 1
        if(self.i > self.max_num):
            raise StopIteration
        return self.i

count = Counter(5)
#for elem in count:
#   print(elem)

print(count.__next__())
print(count.__iter__())
print(next(count))
print(iter(count))
"""

"""---------------------------- Генератори ----------------------------"""

"""
def generator(num, count_num):
    i = 0
    for _ in range(count_num):
        yield num + i
        i += 1

res = generator(100, 10)
print(res, " ")
for _ in res:
    print(_)
"""

"""----------------------------Виклик об'єктів і замикання функції ----------------------------"""

"""
class Helper:
    def __init__(self, work):
        self.work = work
    def __call__(self, work):
        return f"Ill help you with  {self.work}. And then with {work} "

helper = Helper("cooking")
print(helper("work"))
"""

"""
def helper(work):
    work_in_memory = work
    def helper(work):
        return f"Ill help you with  {work_in_memory}. And then with {work} "
    return helper

helper = helper("dungeon")
print(helper("work"))
print(helper("aaaaa"))
"""

"""---------------------------- Декоратори ----------------------------"""

"""
def decorator_checker(func):
    try:
        func()
    except Exception as exc:
        print(f"Problems with {exc}")


@decorator_checker
def calculate(a = int(input("First number:")), b = int(input("Second number:")) ):
    def add(a, b):
        return a + b

    def minus(a, b):
        return a - b

    def multiply(a, b):
        return a * b

    def divide(a, b):
        return a / b

    c = int(input("0.+\n1.-\n2.*\n3./\nChoose option:"))
    def_list = [add(a,b), minus(a,b), multiply(a,b), divide(a,b)]
    print("Result:",def_list[c])
"""

from bs4 import BeautifulSoup
import requests

response = requests.get("https://bank.gov.ua/ua/markets/exchangerates")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("td", {"data-label": "Офіційний курс"})
    for elem in soup_list:
        print(elem)
        print("Конвертер валют - UAH to USD")
        print(f"Курс $: {elem} UAH")
        a = input("Введіть суму(гривні):")


