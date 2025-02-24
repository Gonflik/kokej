# import urllib.request
#
# opener = urllib.request.build_opener()
# response = opener.open("http://httpbin.org/get")
# print(response.read())

# import requests

# response = requests.get("http://httpbin.org/get")
# print(response.content)
# print(f"Datatype: {type(response.content)}")

# response = requests.post("http://httpbin.org/post", data="Test data", headers={"h1": "Test title"})
# print(response.text)


# response = requests.post("http://httpbin.org/post", data={"Test form": "my_form"})
# print(response.text)


# response = requests.get("https://coinmarketcap.com/")
# print(response.text)


# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#    if parse_elem_1.startswith("$"):
#        print(parse_elem_1)


# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#    if parse_elem_1.startswith("$"):
#        for parse_elem_2 in parse_elem_1.split("</span>"):
#            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                print(parse_elem_2)

# res_parse_list = []
# response = requests.get("https://coinmarketcap.com/")
# response_text = response.text
# response_parse = response_text.split("<span>")
# for parse_elem_1 in response_parse:
#    if parse_elem_1.startswith("$"):
#        for parse_elem_2 in parse_elem_1.split("</span>"):
#            if parse_elem_2.startswith("$") and parse_elem_2[1].isdigit():
#                res_parse_list.append(parse_elem_2)
#
# bitcoin = res_parse_list[0]
# print(bitcoin)


# from bs4 import BeautifulSoup
# import requests

# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:
#    soup = BeautifulSoup(response.text, features="html.parser")
#    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
#    for elem in soup_list:
#        print(elem)


# from bs4 import BeautifulSoup
# import requests
#
# response = requests.get("https://coinmarketcap.com/")
# if response.status_code == 200:
#    soup = BeautifulSoup(response.text, features="html.parser")
#    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/markets/"})
#    result = soup_list[0].find("span")
#    print(result.text)


from tkinter import *
from tkinter import messagebox
import random

HEIGHT = 600
WIDTH = 600
tasks = []


def update_listbox():
    list_box.delete(0, END)
    for task in tasks:
        list_box.insert(END, task)


def add_task():
    task = text_input.get()
    if task != "":
        tasks.append(task)
        update_listbox()
    else:
        messagebox.showwarning("Warning", "Write something!")
    text_input.delete(0, END)


def del_one():
    task = list_box.get("active")
    if task in tasks:
        tasks.remove(task)
    update_listbox()


def del_all():
    result = messagebox.askyesno("Confirm", "Are you sure?")
    if result:
        global tasks
        tasks = []
        update_listbox()


def sort_asc():
    tasks.sort()
    update_listbox()


def sort_desc():
    tasks.sort()
    tasks.reverse()
    update_listbox()


def choose_random():
    if len(tasks) > 0:
        task = random.choice(tasks)
        label_display["text"] = task
    else:
        messagebox.showwarning("Warning!!!", "List is empty!")


def num_tasks():
    number_tasks = len(tasks)
    message = "Number tasks: {}".format(number_tasks)
    label_display['text'] = message


root = Tk()
root.title("Note")
root.geometry(f"{WIDTH}x{HEIGHT}")
root.resizable(False, False)

img = PhotoImage(file="image/todo_bg.gif")
bg_label = Label(root, image=img)
bg_label.place(relwidth=1, relheight=1)

root.option_add("*Font", "{Comic Sans MS} 10")
root.option_add("*Background", "white")

frame = Frame(root, bd=10)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

label_title = Label(frame, text="Note Pad", fg="dark blue", font="{Comic Sans MS} 16")
label_title.place(relx=0.4)

label_display = Label(frame, text="")
label_display.place(relx=0.3, rely=0.1)

text_input = Entry(frame, width=1)
text_input.place(relx=0.3, rely=0.15, relwidth=0.6, relheight=0.07)

button_add_task = Button(frame, text="Add task", command=add_task)
button_add_task.place(rely=0.15, relwidth=0.25)

button_del = Button(frame, text="Delete", command=del_one)
button_del.place(rely=0.25, relwidth=0.25)

button_del_all = Button(frame, text="Delete All", command=del_all)
button_del_all.place(rely=0.35, relwidth=0.25)

button_sort_asc = Button(frame, text="Sort (A-Z)", command=sort_asc)
button_sort_asc.place(rely=0.45, relwidth=0.25)

button_sort_desc = Button(frame, text="Sort (Z-A)", command=sort_desc)
button_sort_desc.place(rely=0.55, relwidth=0.25)

button_random = Button(frame, text="Choose random", command=choose_random)
button_random.place(rely=0.65, relwidth=0.25)

button_number_of_tasks = Button(frame, text="Number of tasks", command=num_tasks)
button_number_of_tasks.place(rely=0.75, relwidth=0.25)

button_exit = Button(frame, text="Exit", command=exit)
button_exit.place(rely=0.85, relwidth=0.25)

list_box = Listbox(frame)
list_box.place(relx=0.3, rely=0.24, relwidth=0.6, relheight=0.65)

root.mainloop()

# list1 = [2, 3, 4, 5, 6]
# square = (a**2 for a in list1)
# print(tuple(square))


"""
def Сheckerrr(function):
    try:
        result = function()
    except Exception as exc:
        print(f"Problems with {exc}")
    else:
        print(f"No problems. Result: {result}")


def calculate(a = int(input("first number:")), b = int(input("Second number:"))):
    return a + b

Сheckerrr(calculate())
"""
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
"""

