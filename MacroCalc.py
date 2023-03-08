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
    calories = int(TDEE * .8)
    protein = int(calories * .35) // 4
    fats = int(calories * .2) // 9
    carbs = int(calories * .45) // 4
    print(f"You need to eat {protein}g of protein, {fats}g of fat, and {carbs}g of carbs.")

elif g == 2:
    calories = int(TDEE)
    protein = int(calories * .30) // 4
    fats = int(calories * .15) // 9
    carbs = int(calories * .55) // 4
    print(f"You need to eat {protein}g of protein, {fats}g of fat, and {carbs}g of carbs.")
else:
    calories = int(TDEE * 1.15)
    protein = int(calories * .30) // 4
    fats = int(calories * .2) // 9
    carbs = int(calories * .50) // 4
    print(f"You need to eat {protein}g of protein, {fats}g of fat, and {carbs}g of carbs.")


