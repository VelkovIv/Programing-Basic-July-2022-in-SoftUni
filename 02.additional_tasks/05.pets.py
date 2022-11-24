# Марина обича да пътува. Тя има 3 домашни любимеца (куче, котка и костенурка).
# Когато заминава на пътешествие трябва да съобрази колко храна да им остави, за да не останат гладни.
# Напишете програма, която пресмята колко килограма храна ще изядат всички за времето, в което Марина
# отсъства и дали оставената храна от нея ще им е достатъчна. Всяко животно изяжда определено количество храна на ден.
# Вход
# От конзолата се четат пет реда:
# •	Първи ред – брой дни – цяло число в интервал [1…5000]
# •	Втори ред – оставена храна в килограми – цяло число в интервал [0…100000]
# •	Трети ред – храна на ден за кучето в килограми – реално число в интервал [0.00…100.00]
# •	Четвърти ред – храна на ден за котката в килограми– реално число в интервал [0.00…100.00]
# •	Пети ред – храна на ден за костенурката в грамове – реално число в интервал [0.00…10000.00]
# Изход
# На конзолата трябва да се отпечата на един ред:
# •	Ако оставената храна Е достатъчна:
# o	"{килограма остатък} kilos of food left."
# 	Резултатът трябва да е закръглен към по-ниското цяло число
# •	Ако оставената храна НЕ Е достатъчна:
# o	“{килограма недостигат} more kilos of food are needed.”
# 	Резултатът трябва да е закръглен към по-високото цяло число
from math import floor, ceil

day_numbers = int(input())
food_left_kg = int(input())
dog_food_kg = float(input())
cat_food_kg = float(input())
turtle_food_g = float(input())
dog_food = day_numbers * dog_food_kg
cat_food = day_numbers * cat_food_kg
turtle_food = day_numbers * turtle_food_g / 1000
total_needed_food = dog_food + cat_food + turtle_food
rest_food = abs(food_left_kg - total_needed_food)
if food_left_kg >= total_needed_food:
    rest_food = floor(rest_food)
    print(f"{rest_food} kilos of food left.")
else:
    rest_food = ceil(rest_food)
    print(f"{rest_food} more kilos of food are needed.")