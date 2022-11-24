# Да се напише програма, която чете име на продукт, въведено от потребителя, и проверява дали е плод или зеленчук.
# •	Плодовете "fruit" имат следните възможни стойности:  banana, apple, kiwi, cherry, lemon и grapes;
# •	Зеленчуците "vegetable" имат следните възможни стойности:  tomato, cucumber, pepper и carrot;
# •	Всички останали са "unknown".
# Да се изведе "fruit", "vegetable" или "unknown" според въведения продукт

food = input()

if food == "banana" or food == "apple" or food == "kiwi" or food == "cherry" or food == "lemon" or food == "grapes":
    print("fruit")
elif food == "tomato" or food == "cucumber" or food == "pepper" or food == "carrot":
    print("vegetable")
else:print("unknown")