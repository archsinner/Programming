# Create GUI for calculator
import tkinter as tk

# Create a window
root = tk.Tk()
root.title("Calculator")
# Size the window in percentage of the screen
root.geometry("500x500")
# Create a text box
text_box = tk.Entry(root, width=50, borderwidth=5)
text_box.grid(row=0, column=0, columnspan=3, padx=10, pady=10)
# Creat rows and columns for the buttons in accordance to window size
row_count = 1
column_count = 0
# Create buttons
button_1 = tk.Button(root, text="1", padx=40, pady=20)
button_2 = tk.Button(root, text="2", padx=40, pady=20)
button_3 = tk.Button(root, text="3", padx=40, pady=20)
button_4 = tk.Button(root, text="4", padx=40, pady=20)
button_5 = tk.Button(root, text="5", padx=40, pady=20)
button_6 = tk.Button(root, text="6", padx=40, pady=20)
button_7 = tk.Button(root, text="7", padx=40, pady=20)
button_8 = tk.Button(root, text="8", padx=40, pady=20)
button_9 = tk.Button(root, text="9", padx=40, pady=20)
button_0 = tk.Button(root, text="0", padx=40, pady=20)
button_add = tk.Button(root, text="+", padx=39, pady=20)
button_subtract = tk.Button(root, text="-", padx=41, pady=20)
button_multiply = tk.Button(root, text="*", padx=40, pady=20)
button_divide = tk.Button(root, text="/", padx=40, pady=20)
button_equal = tk.Button(root, text="=", padx=91, pady=20)
button_clear = tk.Button(root, text="Clear", padx=79, pady=20)
# Place the buttons on the window
button_1.grid(row=row_count, column=column_count)
button_2.grid(row=row_count, column=column_count+1)
button_3.grid(row=row_count, column=column_count+2)
row_count += 1
button_4.grid(row=row_count, column=column_count)
button_5.grid(row=row_count, column=column_count+1)
button_6.grid(row=row_count, column=column_count+2)
row_count += 1
button_7.grid(row=row_count, column=column_count)
button_8.grid(row=row_count, column=column_count+1)
button_9.grid(row=row_count, column=column_count+2)
row_count += 1
button_0.grid(row=row_count, column=column_count)
button_add.grid(row=row_count, column=column_count+1)
button_subtract.grid(row=row_count, column=column_count+2)
row_count += 1
button_multiply.grid(row=row_count, column=column_count)
button_divide.grid(row=row_count, column=column_count+1)
button_equal.grid(row=row_count, column=column_count+2)
row_count += 1
button_clear.grid(row=row_count, column=column_count+1)
# Create a function to handle the button clicks
def button_click(number):
    current = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, str(current) + str(number))
# Create a function to handle the clear button
def button_clear_click():
    text_box.delete(0, tk.END)
# Create a function to handle the equal button
def button_equal_click():
    second_number = text_box.get()
    text_box.delete(0, tk.END)
    try:
        answer = eval(first_number + second_number)
        text_box.insert(0, answer)
    except SyntaxError:
        text_box.insert(0, "Error")
# Create a function to handle the add button
def button_add_click():
    global first_number
    first_number = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, "+")
# Create a function to handle the subtract button
def button_subtract_click():
    global first_number
    first_number = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, "-")
# Create a function to handle the multiply button
def button_multiply_click():
    global first_number
    first_number = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, "*")
# Create a function to handle the divide button
def button_divide_click():
    global first_number
    first_number = text_box.get()
    text_box.delete(0, tk.END)
    text_box.insert(0, "/")
# Take button input and show it on the text box
button_1.configure(command=lambda: button_click(1))
button_2.configure(command=lambda: button_click(2))
button_3.configure(command=lambda: button_click(3))
button_4.configure(command=lambda: button_click(4))
button_5.configure(command=lambda: button_click(5))
button_6.configure(command=lambda: button_click(6))
button_7.configure(command=lambda: button_click(7))
button_8.configure(command=lambda: button_click(8))
button_9.configure(command=lambda: button_click(9))
button_0.configure(command=lambda: button_click(0))
button_add.configure(command=lambda: button_add_click())
button_subtract.configure(command=lambda: button_subtract_click())
button_multiply.configure(command=lambda: button_multiply_click())
button_divide.configure(command=lambda: button_divide_click())
button_equal.configure(command=lambda: button_equal_click())
button_clear.configure(command=button_clear_click)

# Run the window
root.mainloop()

