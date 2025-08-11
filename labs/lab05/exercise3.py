# Basic input and output
print("Welcome to the Random Student Selector!")
print("This program will takes the student name randomly")

# Import entire modules
import random

# Getting user input (always returns a string)
class_name = input("Enter your class : ")

# Using imported modules
random_number = random.randint(1, 100)

# Formatted output using string concatenation
print("Class : " , random_number )