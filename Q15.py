#Write a python program to remove all the duplicates from a list

new_list = []

list = ['Zaki','Shahood','Hamza','Hira','Sahar','Shahood','Zaki']

for i in range(len(list)):
    if  list[i] not in new_list:
        new_list.append(list[i])

print(new_list)
