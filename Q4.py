#Write a program that will reverse a four digit number.Also it checks whether the reverse is true.

print("enter number 4 times")

num = []

for i in range(4):
    number = int(input("enter number: "))
    num.append(number)

num_copy = num.copy
reversed_number = num[::-1]

print("reversed numbers: ", reversed_number)

if num_copy == reversed_number:
    print("True")
else:
    print("False")