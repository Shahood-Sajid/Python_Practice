#Write a program that can multiply 2 numbers provided by the user without using the * operator

x = int(input("enter the number you want to multiply: "))
y = int(input("enter the number you want to multiple the previous number from: "))

xy = x

for i in range(y - 1):
    xy += x

print(xy)

