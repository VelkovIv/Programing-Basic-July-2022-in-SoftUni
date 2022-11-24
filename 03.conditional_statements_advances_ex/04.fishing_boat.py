# Тони и приятели много обичат да ходят за риба и са толкова запалени по риболова, че решават да отидат на риболов с кораб.
# Цената за наема на кораба зависи от сезона и броя рибари:
# В зависимост от сезона:
# •	Цената за наем на кораба през пролетта е  3000 лв.;
# •	Цената за наем на кораба през лятото и есента е  4200 лв.;
# •	Цената за наем на кораба през зимата е  2600 лв.
# В зависимост от броя на групата има различна отстъпка:
# •	Ако групата е до 6 човека включително  -  отстъпка от 10%;
# •	Ако групата е от 7 до 11 човека включително  -  отстъпка от 15%;
# •	Ако групата е от 12 нагоре  -  отстъпка от 25%.
# Рибарите ползват допълнително 5% отстъпка, ако са четен брой, освен ако не е есен - тогава нямат допълнителна отстъпка,
# която се начислява след като се приспадне отстъпката по горните критерии.
# Напишете програма, която да пресмята дали рибарите ще съберат достатъчно пари.
# Вход
# От конзолата се четат три реда:
# •	Бюджет на групата - цяло число;
# •	Сезон -  текст: "Spring", "Summer", "Autumn" или "Winter";
# •	Брой рибари - цяло число.
# Изход
# На конзолата да се отпечата следното:
# •	Ако бюджетът е достатъчен:
# "Yes! You have {останалите пари} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# "Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
budget = int(input())
season = input()
fishman = int(input())

discount = 1
people_discount = 1
boat_price = 0
if season == "Spring":
    boat_price = 3000
    if fishman <=6:
        discount = 0.9
    elif 6 < fishman <= 11:
        discount = 0.85
    elif fishman > 12:
        discount = 0.75
    if fishman % 2 == 0:
        people_discount = 0.95
elif season == "Summer":
    boat_price = 4200
    if fishman <= 6:
        discount = 0.9
    elif  6 < fishman <= 11 :
        discount = 0.85
    elif fishman > 12:
        discount = 0.75
    if fishman % 2 == 0:
        people_discount = 0.95
elif season == "Autumn":
    boat_price = 4200
    if fishman <= 6:
        discount = 0.9
    elif 6 < fishman <= 11:
        discount = 0.85
    elif fishman > 12:
        discount = 0.75
elif season == "Winter":
    boat_price = 2600
    if fishman <= 6:
        discount = 0.9
    elif 6 < fishman <= 11:
        discount = 0.85
    elif fishman > 12:
        discount = 0.75
    if fishman % 2 == 0:
        people_discount = 0.95
total_price = boat_price * discount * people_discount
remaining = abs(budget - total_price)
if budget >= total_price:
    print(f"Yes! You have {remaining:.2f} leva left.")
else:
    print(f"Not enough money! You need {remaining:.2f} leva.")