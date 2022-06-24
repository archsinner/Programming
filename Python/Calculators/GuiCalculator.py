# Create a GUI calculator using tkinter
# The calculator will look transparent to the user
# The user will be able to enter numbers and operators
# The user will be able to clear the screen
# The user will be able to quit the program

import tkinter as tk
from tkinter import ttk

class GuiCalculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry("300x300")
        self.resizable(False, False)
        self.create_widgets()
        # Make the window transparent
        self.attributes("-alpha", 0.75)
        self.attributes("-transparentcolor", "white")
        # Make the window resizeable
        self.resizable(True, True)

    def create_widgets(self):
        self.display = tk.StringVar()
        self.display.set("")
        self.display_label = ttk.Label(self, textvariable=self.display, font=("Helvetica", 20))
        self.display_label.grid(row=0, column=0, columnspan=4, sticky="nsew")

        self.button_1 = ttk.Button(self, text="1", command=lambda: self.button_click("1"))
        self.button_1.grid(row=1, column=0, sticky="nsew")
        self.button_2 = ttk.Button(self, text="2", command=lambda: self.button_click("2"))
        self.button_2.grid(row=1, column=1, sticky="nsew")
        self.button_3 = ttk.Button(self, text="3", command=lambda: self.button_click("3"))
        self.button_3.grid(row=1, column=2, sticky="nsew")
        self.button_plus = ttk.Button(self, text="+", command=lambda: self.button_click("+"))
        self.button_plus.grid(row=1, column=3, sticky="nsew")

        self.button_4 = ttk.Button(self, text="4", command=lambda: self.button_click("4"))
        self.button_4.grid(row=2, column=0, sticky="nsew")
        self.button_5 = ttk.Button(self, text="5", command=lambda: self.button_click("5"))
        self.button_5.grid(row=2, column=1, sticky="nsew")
        self.button_6 = ttk.Button(self, text="6", command=lambda: self.button_click("6"))
        self.button_6.grid(row=2, column=2, sticky="nsew")
        self.button_minus = ttk.Button(self, text="-", command=lambda: self.button_click("-"))
        self.button_minus.grid(row=2, column=3, sticky="nsew")

        self.button_7 = ttk.Button(self, text="7", command=lambda: self.button_click("7"))
        self.button_7.grid(row=3, column=0, sticky="nsew")
        self.button_8 = ttk.Button(self, text="8", command=lambda: self.button_click("8"))
        self.button_8.grid(row=3, column=1, sticky="nsew")
        self.button_9 = ttk.Button(self, text="9", command=lambda: self.button_click("9"))
        self.button_9.grid(row=3, column=2, sticky="nsew")
        self.button_multiply = ttk.Button(self, text="*", command=lambda: self.button_click("*"))
        self.button_multiply.grid(row=3, column=3, sticky="nsew")

        self.button_0 = ttk.Button(self, text="0", command=lambda: self.button_click("0"))
        self.button_0.grid(row=4, column=0, sticky="nsew")
        self.button_decimal = ttk.Button(self, text=".", command=lambda: self.button_click("."))
        self.button_decimal.grid(row=4, column=1, sticky="nsew")
        self.button_equals = ttk.Button(self, text="=", command=lambda: self.button_click("="))
        self.button_equals.grid(row=4, column=2, sticky="nsew")
        self.button_divide = ttk.Button(self, text="/", command=lambda: self.button_click("/"))
        self.button_divide.grid(row=4, column=3, sticky="nsew")

        self.button_clear = ttk.Button(self, text="Clear", command=lambda: self.button_click("clear"))
        self.button_clear.grid(row=5, column=0, columnspan=2, sticky="nsew")
        self.button_quit = ttk.Button(self, text="Quit", command=lambda: self.button_click("quit"))
        self.button_quit.grid(row=5, column=2, columnspan=2, sticky="nsew")
        # Make the buttons resizeable with the window
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)
        self.grid_columnconfigure(3, weight=1)
        self.grid_columnconfigure(4, weight=1)
        self.grid_columnconfigure(5, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_rowconfigure(2, weight=1)
        self.grid_rowconfigure(3, weight=1)
        self.grid_rowconfigure(4, weight=1)
        self.grid_rowconfigure(5, weight=1)

    def button_click(self, button):
        if button == "clear":
            self.display.set("")
        elif button == "quit":
            self.destroy()
        else:
            self.display.set(self.display.get() + button)

    def operations(self, num1, num2, operator):
        if operator == "+":
            return num1 + num2
        elif operator == "-":
            return num1 - num2
        elif operator == "*":
            return num1 * num2
        elif operator == "/":
            return num1 / num2

    def calculate(self, num1, num2, operator):
        if operator == "=":
            return self.operations(num1, num2, operator)
        else:
            return self.operations(num1, num2, operator)

if __name__ == "__main__":

    root = GuiCalculator()
    root.mainloop()
    root.destroy()  # destroy the window when done
    exit()
