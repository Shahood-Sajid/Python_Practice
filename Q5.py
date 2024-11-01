#Write a program to find the euclidean distance between two coordinates.

x2 = int(input("enter x2: "))
x1 = int(input("enter x1: "))
y2 = int(input("enter y2: "))
y1 = int(input("enter y1: "))

x = x2 - x1
x_square = x * x

y = y2 - y1
y_square = y * y

euc_dist = (x_square + y_square)**0.5

print("x: ", x, " x_square: ",x_square)
print("y: ", y, " y_square: ",y_square)

print("euc_distance: ", euc_dist)

