# Create a calculator that can add, subtract, multiply and divide two numbers

# Import the necessary modules
import sys
import os
import math

# Get the first number
first_number = float(input("Enter the first number: "))

# Get the second number
second_number = float(input("Enter the second number: "))

# Get the operator
operator = input("Enter the operator: ")

# Calculate the result
if operator == "+":
    result = first_number + second_number
elif operator == "-":
    result = first_number - second_number
elif operator == "*":
    result = first_number * second_number
elif operator == "/":
    result = first_number / second_number

# Print the result
print("The result is: " + str(result))
