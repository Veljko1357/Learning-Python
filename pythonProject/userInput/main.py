# input() = a function that prompts user to enter data
# Data is returned as a string

name = input("What is your name?: ")
age = int(input("how old are you?: "))

age = age + 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY")
print(f"You are {age} years old.")