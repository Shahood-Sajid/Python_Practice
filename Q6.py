#Write a program that will take user input of cost price and selling price and determines whether its a loss or a profit

cost = int(input("enter the cost of product: "))
sell = int(input("enter the selling price of product: "))

if cost > sell:
    print("you are selling this product at this much loss: ", sell - cost)
else:
    print("you are at this much profit: ", sell - cost)