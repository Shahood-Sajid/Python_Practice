#Write a program that will take three digits from the user and add the square of each digit.

input1 = int(input("enter 1st number: "))
input2 = int(input("enter 2nd number: "))
input3 = int(input("enter 3rd number: "))

input1_square = input1 * input1
input2_square = input2 * input2
input3_square = input3 * input3

print("input 1 square: ",input1_square)
print("input 2 square: ",input2_square)
print("input 3 square: ",input3_square)

sum_square = input1_square + input2_square + input3_square

print("sum of these squares: ", sum_square)