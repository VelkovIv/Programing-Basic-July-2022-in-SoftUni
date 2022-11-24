# Петър иска да купи N видеокарти, M процесора и P на брой рам памет.
# Ако броя на видеокартите е по-голям от този на процесорите получава 15% отстъпка от крайната сметка. Важат следните цени:
# · Видеокарта – 250 лв./бр.
# · Процесор – 35% от цената на закупените видеокарти/бр.
# · Рам памет – 10% от цената на закупените видеокарти/бр.
# Да се изчисли нужната сума за закупуване на материалите и да се пресметне дали бюджета ще му стигне.
# Вход
# Входът се състои от четири реда:
# 1. Бюджетът на Петър - реално число в интервала [1.0…100000.0]
# 2. Броят видеокарти - цяло число в интервала [1…100]
# 3. Броят процесори - цяло число в интервала [1…100]
# 4. Броят рам памет - цяло число в интервала [1…100]
# Изход
# На конзолата се отпечатва 1 ред, който трябва да изглежда по следния начин:
# · Ако бюджета е достатъчен:
# "You have {остатъчен бюджет} leva left!"
# · Ако сумата надхвърля бюджета:
# "Not enough money! You need {нужна сума} leva more!"
# Резултатът да се форматира до втория знак след десетичната запетая.

budget = float(input())
videocards_number = int(input())
procesors_number = int(input())
ram_number = int(input())
price_videocards = videocards_number * 250
price_pricesors = procesors_number * price_videocards * 0.35
price_ram = ram_number * price_videocards * 0.1
total_price = price_videocards + price_pricesors + price_ram
if videocards_number > procesors_number :
    discount = total_price * 0.15
    total_price = total_price - discount
diference = abs(budget - total_price)
if budget >= total_price :
    print(f"You have {diference:.2f} leva left!")
else: print(f"Not enough money! You need {diference:.2f} leva more!")
