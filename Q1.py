#User will input (3ages).Find the oldest one


#WorkAround 1
age = []

for i in range(3):
    name = int(input("enter age: "))
    age.append(name)

print("all ages: ", age)
print("oldest one:", max(age))

#WorkAround 2
max_age = 0

age = []

for i in range(3):
    
    name = int(input("enter age: "))
    age.append(name)

for i in age:
    if i > max_age:
        max_age = i

print("oldest one",max_age)