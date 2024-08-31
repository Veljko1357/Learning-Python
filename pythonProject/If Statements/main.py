age = int(input("Enter your age: "))


#order matters
if age >= 100:
    print("You are too old to sign up")
elif age >= 18:
    print("You are now signed up!")
elif age < 0:
    print("You haven't been born yet")
else:
    print("You must be 18+ to sign up")


response = input("Would you like some food? (Y/N)")

if response == "Y":
    print("Have some food")
else:
    print("No food for you")


name = input("Enter your name: ")

if name == "":
    print("YOU DID NOT TYPE IN YOUR NAME")
else:
    print(f"Hello {name}")


for_sale = True 

if for_sale:
    print("This item is for sale")
else:
    print("This item is NOT for sale")