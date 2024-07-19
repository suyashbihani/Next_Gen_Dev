import tkinter as tk
from tkinter import messagebox

def add():
    item = entry.get()
    if item:
        var = tk.BooleanVar()
        checkbox = tk.Checkbutton(check_frame, text=item, variable=var, bg='#f0f0f0', font=('Arial', 12))
        checkbox.pack(anchor='w', pady=5, padx=10)
        checkboxes.append((checkbox, var))
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter some text")

def delete():
    remove = [x for x, (checkbox, var) in enumerate(checkboxes) if var.get()]

    for x in reversed(remove):
        checkbox, var = checkboxes[x]
        checkbox.destroy()
        del checkboxes[x]

def update():
    def save():
        for i, (entry, var) in enumerate(entries):
            checkbox, _ = checkboxes[i]
            checkbox.config(text=entry.get())
        updateW.destroy()

    updateW = tk.Toplevel(root)
    updateW.title("Update Checkboxes")
    updateW.geometry("350x400")
    updateW.configure(bg='#e0e0e0')

    tk.Label(updateW, text="Edit checkbox labels:", bg='#e0e0e0', font=('Arial', 12, 'bold')).pack(pady=10)

    entries = []
    for checkbox, var in checkboxes:
        entry = tk.Entry(updateW, width=30, font=('Arial', 12))
        entry.pack(pady=5, padx=10)
        entry.insert(0, checkbox.cget("text"))
        entries.append((entry, var))

    save_button = tk.Button(updateW, text="Save Changes", command=save, font=('Arial', 12), bg='#4CAF50', fg='white', padx=10, pady=5)
    save_button.pack(pady=10)

root = tk.Tk()
root.title("To-Do List")
root.geometry("400x500")
root.configure(bg='#f0f0f0')

frame = tk.Frame(root, bg='#f0f0f0')
frame.pack(fill='both', expand=True)

entry = tk.Entry(frame, width=30, font=('Arial', 12))
entry.pack(pady=15)

add_button = tk.Button(frame, text="Add", command=add, font=('Arial', 12), bg='#4CAF50', fg='white', padx=10, pady=5)
add_button.pack(pady=5)

update_button = tk.Button(frame, text="Update", command=update, font=('Arial', 12), bg='#2196F3', fg='white', padx=10, pady=5)
update_button.pack(pady=5)

check_frame = tk.Frame(frame, bg='#f0f0f0')
check_frame.pack(fill='both', expand=True)

checkboxes = []

bottom_frame = tk.Frame(root, bg='#f0f0f0')
bottom_frame.pack(side='bottom', fill='x', pady=10)

delete_button = tk.Button(bottom_frame, text="Delete", command=delete, font=('Arial', 12), bg='#f44336', fg='white', padx=10, pady=5)
delete_button.pack()

root.mainloop()