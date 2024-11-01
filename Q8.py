# Write a program that will determine weather when the value of temperature and humidity is provided by the user.
# TEMPERATURE(C)      HUMIDITY(%)      WEATHER

#       >= 30                             >=90                Hot and Humid
#       >= 30                             < 90                 Hot
#       <30                                >= 90               Cool and Humid
#       <30                                 <90                 Cool


temp = int(input("enter the temperature: "))
humid = int(input("enter the humidity: "))

if temp < 30 and humid < 90:
    print("cool")
elif temp < 30 and humid >= 90:
    print("Cool and Humid")
elif temp >= 30 and temp < 90:
    print("Hot")
else:
    print("Hot and Humid")