import tkinter as tk
from tkinter import messagebox
import math

expression = ""

def press(num):
    global expression
    expression += str(num)
    entry_text.set(expression)

def clear():
    global expression
    expression = ""
    entry_text.set(expression)

def calculate():
    global expression
    try:
        # Evaluate the expression
        result = eval(expression)
        entry_text.set(result)
        expression = str(result)
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")
        clear()
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        clear()

def square():
    global expression
    try:
        result = eval(expression) ** 2
        entry_text.set(result)
        expression = str(result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        clear()

def sqrt():
    global expression
    try:
        value = eval(expression)
        if value < 0:
            messagebox.showerror("Error", "Cannot take square root of negative number")
            clear()
            return
        result = math.sqrt(value)
        entry_text.set(result)
        expression = str(result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        clear()

def power():
    global expression
    try:

        result = eval(expression)
        entry_text.set(result)
        expression = str(result)
    except Exception:
        messagebox.showerror("Error", "Invalid Input")
        clear()

root = tk.Tk()
root.title("Smart Calculator")
root.geometry("350x450")
root.resizable(False, False)

entry_text = tk.StringVar()

entry = tk.Entry(root, textvariable=entry_text, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.pack(fill="both", ipadx=8, pady=10, padx=10)

buttons = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', '.', '=', '+']
]

for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for btn in row:
        if btn == "=":
            b = tk.Button(frame, text=btn, font=("Arial", 18), fg="white", bg="green", command=calculate)
        else:
            b = tk.Button(frame, text=btn, font=("Arial", 18), command=lambda x=btn: press(x))
        b.pack(side="left", expand=True, fill="both")

frame2 = tk.Frame(root)
frame2.pack(expand=True, fill="both", pady=5)
tk.Button(frame2, text="C", font=("Arial", 18), fg="white", bg="red", command=clear).pack(side="left", expand=True, fill="both")
tk.Button(frame2, text="x²", font=("Arial", 18), fg="white", bg="blue", command=square).pack(side="left", expand=True, fill="both")
tk.Button(frame2, text="√", font=("Arial", 18), fg="white", bg="blue", command=sqrt).pack(side="left", expand=True, fill="both")
tk.Button(frame2, text="**", font=("Arial", 18), fg="white", bg="purple", command=lambda: press("**")).pack(side="left", expand=True, fill="both")

tk.Button(root, text="Exit", font=("Arial", 14), bg="gray", fg="white", command=root.destroy).pack(fill="both", pady=5, padx=10)

root.mainloop()
