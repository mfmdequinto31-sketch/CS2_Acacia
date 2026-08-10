import math
print("Calculate the distance between two points")
x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))
d = round(math.sqrt((pow((x2 - x1),2)) + pow((y2 - y1),2)),2)
print("The distance between two points is,", d)