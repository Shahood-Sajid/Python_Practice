#User will input (2numbers).Write a program to swap the numbers

input1 = int(input("enter 1st number: "))
input2 = int(input("enter 2nd number: "))

print("num 1 before swap",input1, " and num 2 before swap ", input2)
swap = input1
input1 = input2
input2 = swap

print("now num 1 is ",input1, " and num 2 is ",input2)