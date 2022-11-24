purchaised_dog_food_kg = int(input())
purchaised_dog_food_grams = purchaised_dog_food_kg * 1000
command = input()

while command != "Adopted":
    dailly_dog_food = int(command)
    purchaised_dog_food_grams -= dailly_dog_food

    command = input()
left_over = abs(purchaised_dog_food_grams)
if purchaised_dog_food_grams >= 0:
    print(f"Food is enough! Leftovers: {left_over} grams.")
else:
    print(f"Food is not enough. You need {left_over} grams more.")