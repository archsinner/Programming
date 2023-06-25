# Create a GUI calculator using Tkinter

from tkinter import *

# Create a window
window = Tk()
window.title("Calculator")
window.geometry("330x425")

# Create a output box that scales with the window by percentage
output = Entry(window, width=50, borderwidth=5)
output.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# Create a function to add a number to the output box
def button_click(number):
    current = output.get()
    output.delete(0, END)
    output.insert(0, str(current) + str(number))

# Create a function to clear the output box
def button_clear():
    output.delete(0, END)

# Create a function to add
def button_add():
    first_number = output.get()
    global f_num
    global math
    math = "addition"
    f_num = int(first_number)
    output.delete(0, END)

# Create a function to subtract
def button_subtract():
    first_number = output.get()
    global f_num
    global math
    math = "subtraction"
    f_num = int(first_number)
    output.delete(0, END)

# Create a function to multiply
def button_multiply():
    first_number = output.get()
    global f_num
    global math
    math = "multiplication"
    f_num = int(first_number)
    output.delete(0, END)

# Create a function to divide
def button_divide():
    first_number = output.get()
    global f_num
    global math
    math = "division"
    f_num = int(first_number)
    output.delete(0, END)

# Create a function to equal
def button_equal():
    second_number = output.get()
    output.delete(0, END)

    if math == "addition":
        output.insert(0, f_num + int(second_number))
    elif math == "subtraction":
        output.insert(0, f_num - int(second_number))
    elif math == "multiplication":
        output.insert(0, f_num * int(second_number))
    elif math == "division":
        output.insert(0, f_num / int(second_number))

# Create buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
button_4 = Button(window, text="4", padx=40, pady=20, command=lambda: button_click(4))
button_5 = Button(window, text="5", padx=40, pady=20, command=lambda: button_click(5))
button_6 = Button(window, text="6", padx=40, pady=20, command=lambda: button_click(6))
button_7 = Button(window, text="7", padx=40, pady=20, command=lambda: button_click(7))
button_8 = Button(window, text="8", padx=40, pady=20, command=lambda: button_click(8))
button_9 = Button(window, text="9", padx=40, pady=20, command=lambda: button_click(9))
button_0 = Button(window, text="0", padx=40, pady=20, command=lambda: button_click(0))
button_add = Button(window, text="+", padx=40, pady=20, command=button_add)
button_equal = Button(window, text="=", padx=40, pady=20, command=button_equal)
button_clear = Button(window, text="Clear", padx=40, pady=20, command=button_clear)
button_subtract = Button(window, text="-", padx=40, pady=20, command=button_subtract)
button_multiply = Button(window, text="*", padx=40, pady=20, command=button_multiply)
button_divide = Button(window, text="/", padx=40, pady=20, command=button_divide)

# Put buttons on the screen
button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_0.grid(row=4, column=0)
button_add.grid(row=4, column=2)
button_equal.grid(row=5, column=0)
button_clear.grid(row=7, column=1)
button_subtract.grid(row=5, column=1)
button_multiply.grid(row=4, column=1)
button_divide.grid(row=5, column=2)

# Reverse the colors of the calculator
window.config(background="black")
output.config(background="black", fg="white")
button_1.config(background="black", fg="white")
button_2.config(background="black", fg="white")
button_3.config(background="black", fg="white")
button_4.config(background="black", fg="white")
button_5.config(background="black", fg="white")
button_6.config(background="black", fg="white")
button_7.config(background="black", fg="white")
button_8.config(background="black", fg="white")
button_9.config(background="black", fg="white")
button_0.config(background="black", fg="white")
button_add.config(background="black", fg="white")
button_equal.config(background="black", fg="white")
button_clear.config(background="black", fg="white")
button_subtract.config(background="black", fg="white")
button_multiply.config(background="black", fg="white")
button_divide.config(background="black", fg="white")

# Add 10 percent opacity to the calculator while resizing with blur
window.attributes('-alpha', 0.95)

# make title bar dark
window.config(bg="#2e2e2e")


# lock the window size
window.resizable(width=False, height=False)


# run the window
window.mainloop()