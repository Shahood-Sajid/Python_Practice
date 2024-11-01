# Write a program that keeps on accepting a number from the user until the user enters Zero. Display the sum and average of all the numbers.


number = int(input("enter a number: "))

num_list = []
while number != 0:
    num_list.append(number)
    number = int(input("enter a number: "))

sum_list = 0
for i in num_list:
    sum_list += i

avg = sum_list / len(num_list)

print("total sum: ",sum_list)
print("avg: ",avg)
