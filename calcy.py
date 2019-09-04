## Simple Calculator
import tkinter as tk
from tkinter import messagebox

mainWindow = tk.Tk()
mainWindow .title("Calculator")

label = tk.Label(mainWindow , text="Enter first number")
label.pack()

first_number_entry = tk.Entry(mainWindow )
first_number_entry.pack()

label2 = tk.Label(mainWindow , text="Enter second number")
label2.pack()

second_number_entry = tk.Entry(mainWindow )
second_number_entry.pack()

operations = tk.Label(mainWindow , text="Operations")
operations.pack()


def addition():
    first, second = takeValueInput()
    result = first + second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                            str(result))

def subtract():
    first, second = takeValueInput()
    result = first - second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))


def multiply():
    first, second = takeValueInput()
    result = first * second
    # print(first + second)
    result_label.config(text="Operations result is: " +
                             str(result))


def divide():
    first, second = takeValueInput()

    if second == 0:
        messagebox.showerror("Error", "Cannot divide the value by 0.")
    else:
        result = first / second
        # print(first + second)
        result = round(result, 2)
        result_label.config(text="Operations result is: " +
                                 str(result))


def takeValueInput():
    first = first_number_entry.get()
    second = second_number_entry.get()

    try:
        first = int(first)
        second = int(second)

        return first, second
    except ValueError:
        if ((len(first_number_entry.get()) == 0) or (len(second_number_entry.get()) == 0)):
            messagebox.showerror("Error", "Please enter a value")
        else:
            messagebox.showerror("Error", "Enter only integer value")
        quit(0)
##making of the buttons

button = tk.Button(mainWindow , text="+",
                            command=lambda: addition())
button.pack()

button = tk.Button(mainWindow , text="-",
                         command=lambda: subtract())
button.pack()

button = tk.Button(mainWindow , text="*",
                            command=lambda: multiply())
button.pack()

button = tk.Button(mainWindow , text="/",
                            command=lambda: divide())
button.pack()

result_label = tk.Label(mainWindow , text="Operations result is:")
result_label.pack()
mainWindow.mainloop()
