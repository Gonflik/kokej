from tkinter import *

exp = ""

HEIGHT = 600
WIDTH = 600


def press(num):
    global exp
    exp = exp + str(num)
    equation.set(exp)


def equal():
    try:
        global exp
        total = str(eval(exp))
        equation.set(total)
        exp = ""
    except:
        equation.set(" Error! ")
        exp = ""


def clear():
    global exp
    exp = ""
    equation.set("")


if __name__ == "__main__":
    root = Tk()
    root.title("Calculator")
    root.geometry(f"{WIDTH}x{HEIGHT}")
    root.resizable(False, False)

    equation = StringVar()

    img = PhotoImage(file="img/bgg.gif")
    bg_label = Label(root, image=img)
    bg_label.place(relwidth=1, relheight=1)

    frame = Frame(root, bd=10)
    frame.place(rely=0.1, relx=0.1, relheight=0.8, relwidth=0.8)

    entry_box = Entry(frame, textvariable=equation, font="{Comic Sans MS} 11")
    entry_box.grid(columnspan=4, ipadx=150, ipady=20)

    button1 = Button(frame, text="1", fg="white", bg="purple", command=lambda: press(1), height=4, width=12)
    button1.grid(row=2, column=0)

    button2 = Button(frame, text="2", fg="white", bg="purple", command=lambda: press(2), height=4, width=12)
    button2.grid(row=2, column=1)

    button3 = Button(frame, text="3", fg="white", bg="purple", command=lambda: press(3), height=4, width=12)
    button3.grid(row=2, column=2)

    button4 = Button(frame, text="4", fg="white", bg="purple", command=lambda: press(4), height=4, width=12)
    button4.grid(row=3, column=0)

    button5 = Button(frame, text="5", fg="white", bg="purple", command=lambda: press(5), height=4, width=12)
    button5.grid(row=3, column=1)

    button6 = Button(frame, text="6", fg="white", bg="purple", command=lambda: press(6), height=4, width=12)
    button6.grid(row=3, column=2)

    button7 = Button(frame, text="7", fg="white", bg="purple", command=lambda: press(7), height=4, width=12)
    button7.grid(row=4, column=0)

    button8 = Button(frame, text="8", fg="white", bg="purple", command=lambda: press(8), height=4, width=12)
    button8.grid(row=4, column=1)

    button9 = Button(frame, text="9", fg="white", bg="purple", command=lambda: press(9), height=4, width=12)
    button9.grid(row=4, column=2)

    button0 = Button(frame, text="0", fg="white", bg="purple", command=lambda: press(0), height=4, width=12)
    button0.grid(row=5, column=0)

    plus = Button(frame, text="+", fg="white", bg="purple", command=lambda: press("+"), height=4, width=12)
    plus.grid(row=2, column=3)

    minus = Button(frame, text="-", fg="white", bg="purple", command=lambda: press("-"), height=4, width=12)
    minus.grid(row=3, column=3)

    multiply = Button(frame, text="*", fg="white", bg="purple", command=lambda: press("*"), height=4, width=12)
    multiply.grid(row=4, column=3)

    divide = Button(frame, text="/", fg="white", bg="purple", command=lambda: press("/"), height=4, width=12)
    divide.grid(row=5, column=3)

    equal = Button(frame, text="=", fg="white", bg="purple", command=equal, height=4, width=12)
    equal.grid(row=5, column=2)

    clear = Button(frame, text="Clear", fg="white", bg="purple", command=clear, height=4, width=12)
    clear.grid(row=5, column="1")

    point = Button(frame, text=".", fg="white", bg="purple", command=lambda: press("."), height=4, width=12)
    point.grid(row=6, column=0)

    root.mainloop()
