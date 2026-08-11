import math

# print the problem that the user has
print("Calculate the distance between two points")

# Ask the user to enter the x_coordinates of the first and second point
x1 = int(input("Enter x1:"))
x2 = int(input("Enter x2:"))

# Ask the user to enter the y_coordinate of the first and second point
y1 = int(input("Enter y1:"))
y2 = int(input("Enter y2:"))

# compute the distance using the distance formula
distance = round(math.sqrt((pow((x2 - x1),2)) + pow((y2 - y1),2)),2)

# print the distance rounded to two points
print("The distance between two points is,", d)
