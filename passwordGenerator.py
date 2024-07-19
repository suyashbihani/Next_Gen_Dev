import tkinter as tk
from tkinter import StringVar, messagebox
import random
import string

def generate_password():
    length = int(len.get())
    if length < 6:
        messagebox.showwarning("Warning", "Password length should be at least 6 characters.")
        return

    c = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(c) for i in range(length))
    pw.set(password)

app = tk.Tk()
app.title("Password Generator")
app.geometry("275x175")

tk.Label(app, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
len = StringVar(value="8")
tk.Entry(app, textvariable=len, width=10).grid(row=0, column=1, padx=10, pady=10)


tk.Button(app, text="Generate Password", command=generate_password).grid(row=1, column=0, columnspan=2, padx=10, pady=10)


pw = StringVar()
tk.Entry(app, textvariable=pw, width=40, state="readonly").grid(row=2, column=0, columnspan=2, padx=10, pady=10)

app.mainloop()
