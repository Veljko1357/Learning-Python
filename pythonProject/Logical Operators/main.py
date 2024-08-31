#Logical operators evluate multiple condition (or, and, not)
    # or = at least one condition must be True
    # and - both conditions must be True
    # not - inverts the conditions (not False, not True)

#or operator

# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is canceled")
# else: 
#     print("The outdoor event is still scheduled")

#and operator 

# temp = 11
# is_sunny = True

# if temp >= 28 and is_sunny:
#     print("It is hot outside")
#     print("It is sunny")
# elif temp <= 0 and is_sunny:
#     print("it is cold outside")
#     print("it is sunny")
# elif 28 > temp > 0 and is_sunny:
#     print("it is warm outside")

#not operator

temp = 11
is_sunny = False

if temp >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp <= 0 and is_sunny:
    print("it is cold outside")
    print("it is sunny")
elif 28 > temp > 0 and is_sunny:
    print("it is warm outside")
elif temp >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is clody")
elif temp <= 0 and not is_sunny:
    print("it is cold outside")
    print("it is cloudy")
elif 28 > temp > 0 and not is_sunny:
    print("it is warm outside")
    print("It is cloudy")