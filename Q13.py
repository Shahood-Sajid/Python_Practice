#Find the length of a given string without using the len() function. 

string = input("enter a string: ")

count = 0
for i in string:
    count += 1

print("length of string: ", count)