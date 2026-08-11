import math
# print
print("Calculate the distance between two points")

# input
x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))

# input
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))

# answer
distance = round(math.sqrt((pow((x2 - x1),2)) + pow((y2 - y1),2)),2)

# print
print("The distance between two points is,", d)
