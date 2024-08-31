# AKA ternary operators - A one line shortcuts for If statements
# print or assign one of two values based on condition
# if X condition else Y


num = 5
a = 6
b = 7
age = 13
temperature = 30
user_role = "guest"
# print("Positive" if num > 0 else "Negative")
# result = "Even" if num % 2 == 0 else "Odd"
# max_num = a if a > b else b
# min = a if a < b else b
# status = "Adult" if age >= 18 else "Child"
# weather = "Hot" if temperature > 20 else "Cold"
acces_level = "Full access" if user_role =="admin" else "Limited access"
print(acces_level)