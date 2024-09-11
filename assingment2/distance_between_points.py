# Write a Python program to calculate the distance between the points (x1, y1) and (x2, y2).

import math

def calculate_distance(x1,y1,x2,y2):
    return math.sqrt(x2-x1)**2 + (y2-y1)**2

x1=float(input("enter x1:"))
x2=float(input("enter x2:"))
y1=float(input("enter y1:"))
y2=float(input("enter y2:"))




distance = calculate_distance(x1,y1,x2,y2)

print(f"the distance between the points {x1} - {y1} and {x2} - {y2} is: {distance}")
