print("Welcome to the Circle Calculator!")
print("This program will display circle area and circumference.")

# Import entire modules
import math

radius_of_circle = float(input("Enter the radius of the circle: "))

area = math.pi * radius_of_circle ** 2
circumference = 2.0 * math.pi * radius_of_circle

print("Area of the circle            : " ,area)
print("Circumference of the circle   : " , circumference)