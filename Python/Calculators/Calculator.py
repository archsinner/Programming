# Create a gui calculator
# This is a calculator that can be used to do basic math

from re import T
import tkinter as tk
from tkinter import ttk
# Create window GUI
window = tk.Tk()
window.title("Calculator")
# Create a frame for the buttons
frame = tk.Frame(window, width=300, height=300)
frame.pack()
# Create a label to display the result
result = tk.StringVar()
result_label = ttk.Label(frame, textvariable=result)
result_label.grid(row=0, column=0, columnspan=4)

# Create a string variable to hold the result
result = tk.StringVar()

# Create a label to display the result
label = ttk.Label(frame, textvariable=result)
label.grid(column=2, row=1, sticky=(tk.W, tk.E))

# Create a function to handle the button clicks
def click(number):
    current = result.get()
    result.set(current + str(number))

# Create a function to handle the clear button
def clear():
    result.set("")

# Create a function to handle the equals button
def equals():
    # Get the current value
    current = result.get()
    # Evaluate the expression
    result.set(eval(current))

# Create a function to handle the backspace button
def backspace():
    current = result.get()
    result.set(current[:-1])

# Create a function to handle the decimal button
def decimal():
    current = result.get()
    result.set(current + ".")

# Create a function to handle the plus button
def plus():
    current = result.get()
    result.set(current + "+")

# Create a function to handle the minus button
def minus():
    current = result.get()
    result.set(current + "-")

# Create a function to handle the multiply button
def multiply():
    current = result.get()
    result.set(current + "*")

# Create a function to handle the divide button
def divide():
    current = result.get()
    result.set(current + "/")

# Create a function to handle the power button
def power():
    current = result.get()
    result.set(current + "**")

# Create a function to handle the square button
def square():
    current = result.get()
    result.set(current + "**2")

# Create a function to handle the cube button
def cube():
    current = result.get()
    result.set(current + "**3")

# Create a function to handle the factorial button
def factorial():
    current = result.get()
    result.set(current + "!")

# Create a function to handle the sin button
def sin():
    current = result.get()
    result.set(current + "sin")

# Create a function to handle the cos button
def cos():
    current = result.get()
    result.set(current + "cos")

# Create a function to handle the tan button
def tan():
    current = result.get()
    result.set(current + "tan")

# Create a function to handle the log button
def log():
    current = result.get()
    result.set(current + "log")

# Create a function to handle the ln button
def ln():
    current = result.get()
    result.set(current + "ln")

# Create a function to handle the pi button
def pi():
    current = result.get()
    result.set(current + "pi")

# Create a function to handle the e button
def e():
    current = result.get()
    result.set(current + "e")

# Create a function to handle the factorial button
def factorial():
    current = result.get()
    result.set(current + "!")

# Create a function to handle the x^2 button
def square():
    current = result.get()
    result.set(current + "**2")

# Create a button to handle the 0 button
button0 = ttk.Button(window, text="0", command=lambda: click(0))
button0.grid(column=0, row=2, sticky=(tk.W, tk.E))


# Create a button to handle the 1 button
button1 = ttk.Button(window, text="1", command=lambda: click(1))
button1.grid(column=0, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the 2 button
button2 = ttk.Button(window, text="2", command=lambda: click(2))
button2.grid(column=1, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the 3 button
button3 = ttk.Button(window, text="3", command=lambda: click(3))
button3.grid(column=2, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the 4 button
button4 = ttk.Button(window, text="4", command=lambda: click(4))
button4.grid(column=0, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the 5 button
button5 = ttk.Button(window, text="5", command=lambda: click(5))
button5.grid(column=1, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the 6 button
button6 = ttk.Button(window, text="6", command=lambda: click(6))
button6.grid(column=2, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the 7 button
button7 = ttk.Button(window, text="7", command=lambda: click(7))
button7.grid(column=0, row=3, sticky=(tk.W, tk.E))


# Create a button to handle the 8 button
button8 = ttk.Button(window, text="8", command=lambda: click(8))
button8.grid(column=1, row=3, sticky=(tk.W, tk.E))


# Create a button to handle the 9 button
button9 = ttk.Button(window, text="9", command=lambda: click(9))
button9.grid(column=2, row=3, sticky=(tk.W, tk.E))


# Create a button to handle the decimal button
buttonDecimal = ttk.Button(window, text=".", command=decimal)
buttonDecimal.grid(column=0, row=4, sticky=(tk.W, tk.E))


# Create a button to handle the plus button
buttonPlus = ttk.Button(window, text="+", command=plus)
buttonPlus.grid(column=3, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the minus button
buttonMinus = ttk.Button(window, text="-", command=minus)
buttonMinus.grid(column=3, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the multiply button
buttonMultiply = ttk.Button(window, text="*", command=multiply)
buttonMultiply.grid(column=3, row=2, sticky=(tk.W, tk.E))


# Create a button to handle the divide button
buttonDivide = ttk.Button(window, text="/", command=divide)
buttonDivide.grid(column=3, row=3, sticky=(tk.W, tk.E))


# Create a button to handle the power button
buttonPower = ttk.Button(window, text="^", command=power)
buttonPower.grid(column=3, row=4, sticky=(tk.W, tk.E))

# Create a button to handle the square button
buttonSquare = ttk.Button(window, text="x^2", command=square)
buttonSquare.grid(column=4, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the cube button
buttonCube = ttk.Button(window, text="x^3", command=cube)
buttonCube.grid(column=4, row=2, sticky=(tk.W, tk.E))


# Create a button to handle the factorial button
buttonFactorial = ttk.Button(window, text="!", command=factorial)
buttonFactorial.grid(column=4, row=3, sticky=(tk.W, tk.E))


# Create a button to handle the sin button
buttonSin = ttk.Button(window, text="sin", command=sin)
buttonSin.grid(column=4, row=4, sticky=(tk.W, tk.E))


# Create a button to handle the cos button
buttonCos = ttk.Button(window, text="cos", command=cos)
buttonCos.grid(column=5, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the tan button
buttonTan = ttk.Button(window, text="tan", command=tan)
buttonTan.grid(column=5, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the ln button
buttonLn = ttk.Button(window, text="ln", command=ln)
buttonLn.grid(column=5, row=2, sticky=(tk.W, tk.E))


# Create a button to handle the log button
buttonLog = ttk.Button(window, text="log", command=log)
buttonLog.grid(column=5, row=3, sticky=(tk.W, tk.E))



# Create a button to handle the e button
buttonE = ttk.Button(window, text="e", command=e)
buttonE.grid(column=5, row=4, sticky=(tk.W, tk.E))


# Create a button to handle the pi button
buttonPi = ttk.Button(window, text="π", command=pi)
buttonPi.grid(column=6, row=0, sticky=(tk.W, tk.E))


# Create a button to handle the clear button
buttonClear = ttk.Button(window, text="C", command=clear)
buttonClear.grid(column=6, row=1, sticky=(tk.W, tk.E))


# Create a button to handle the equals button
buttonEquals = ttk.Button(window, text="=", command=equals)
buttonEquals.grid(column=6, row=3, sticky=(tk.W, tk.E))

# Create window to display the answer
answerWindow = tk.Toplevel(window)
answerWindow.title("Answer")
answerWindow.geometry("200x100")
answerWindow.resizable(0, 0)
answerWindow.wm_attributes("-topmost", 1)
answerWindow.wm_attributes("-disabled", 1)
answerWindow.wm_attributes("-transparentcolor", "white")
answerWindow.wm_attributes("-alpha", 0.5)

# Create the calculator
window.mainloop()
