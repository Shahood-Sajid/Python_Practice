#Extract username from a given email.  Eg if the email is nitish24singh@gmail.com then the username should be nitish24singh

email = input("enter your email: ")

seperated = email.split('@')

print(seperated[0])