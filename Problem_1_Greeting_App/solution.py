# your code here
name = input("please enter your name: ")
food = input("your favorite food: ")
year = input("current year: ")
age = input("your age:")
print(f"Hi {name}, thank you for being part of our online family!")
year_of_birth = int(year) - int(age)
choice = input("do you want to know your year of birth? ")
if choice == "yes":
   print(f"{year_of_birth} is your year of birth.")
print("thanks for visiting!")
