name = input("Enter your name: ")

age = int(input("Enter your age: "))

current_year = 2024
birth_year = current_year - age

print("Hello "+ name + "! You were born in "+ str(birth_year) +".")

if age > 17:
  print("You are eligible to vote!")
else:
  print("You are ineligible to vote!")
