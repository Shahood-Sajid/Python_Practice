#Write a program to find the sum of first n numbers, where n will be provided by the user. Eg if the user provides n=10 the output should be 55.

num_range = int(input("enter the number range: "))

sum = 0
for i in range(num_range + 1):
    sum += i

print("sum: ", sum)