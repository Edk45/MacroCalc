h = int(input("What is your height in centimeters? "))
w = int(input("What is your weight in kilograms? "))
a = int(input("What is your age? "))
ac = int(input("What is your activity level from 1 to 4? "))
g = int(input("What is your goal? "))


REE = 5 + (10 * w) + (6.25 * h) - (5 * a)


if ac == 1:
    TDEE = REE * 1.2
elif ac == 2:
   TDEE = REE * 1.375
elif ac == 3:
    TDEE = REE * 1.55
else:
    TDEE = REE * 1.725

if g == 1:
    goal = int(TDEE * .8)
elif g == 2:
    goal = int(TDEE)
else:
    goal = int(TDEE * 1.15)



