from datetime import datetime

Name = input("Enter your name : ")
Age = int(input("Enter your age : "))
current = datetime.now()
year = current.strftime("%Y")
final_age = 100 - Age
decade =int(year) + final_age

print("Hi "+Name+" we wish you have a wonderful day. ")
print("A fun fact for you.You will turn 100 in the year",decade)
