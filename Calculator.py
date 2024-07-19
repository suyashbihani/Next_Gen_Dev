from tkinter import *

me = Tk()
me.geometry("355x460")
me.title("CALCULATOR")

input = StringVar()
expression = ""

def clickbut(number):
    global expression
    expression += str(number)
    input.set(expression)

def equlbut():
    global expression
    try:
        result = str(eval(expression))
        input.set(result)
        expression = result
    except Exception as e:
        input.set("Error")
        expression = ''

def clrbut():
    global expression
    expression = ''
    input.set('')


metext = Entry(me, font=("Courier New", 12, 'bold'), textvar=input, width=30, bd=25, bg='powder blue')
metext.pack()

button = [
    (7, 10, 100), (4, 10, 170), (1, 10, 240),
    (8, 75, 100), (5, 75, 170), (2, 75, 240),
    (9, 140, 100), (6, 140, 170), (3, 140, 240),
    (0, 10, 310)
]

for (num, x, y) in button:
    Button(me, padx=14, pady=14, bd=4, bg='white', text=str(num), command=lambda num=num: clickbut(num), font=("Courier New", 16, 'bold')).place(x=x, y=y)

operator_b = [
    ('+', 205, 100), ('-', 205, 170), ('*', 205, 240), ('/', 205, 310)
]

for (op, x, y) in operator_b:
    Button(me, padx=14, pady=14, bd=4, bg='white', text=op, command=lambda op=op: clickbut(op), font=("Courier New", 16, 'bold')).place(x=x, y=y)

Button(me, padx=14, pady=119, bd=4, bg='white', text="CE", command=clrbut, font=("Courier New", 16, 'bold')).place(x=270, y=100)
Button(me, padx=151, pady=14, bd=4, bg='white', text="=", command=equlbut, font=("Courier New", 16, 'bold')).place(x=10, y=380)
Button(me, padx=46, pady=14, bd=4, bg='white', text=".", command=lambda: clickbut('.'), font=("Courier New", 16, 'bold')).place(x=75, y=310)

me.mainloop()
