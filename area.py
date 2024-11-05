#Calculating the area of circle
import math

def calculate_area_circle(radius):
    area = math.pi * radius ** 2
    return area

#calling the function
radius = 5
area = calculate_area_circle(radius)
print("The area of a circle is", area)