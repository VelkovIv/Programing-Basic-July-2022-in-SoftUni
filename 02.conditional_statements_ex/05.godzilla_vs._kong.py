# Снимките за дългоочаквания филм "Годзила срещу Конг" започват
# Сценаристът Адам Уингард ви моли да напишете програма, която да изчисли, дали предвидените средства са достатъчни за снимането
# на филма. За снимките ще бъдат нужни определен брой статисти, облекло за всеки един статист и декор.
# Известно е, че:
# · Декорът за филма е на стойност 10% от бюджета.
# · При повече от 150 статиста, има отстъпка за облеклото на стойност 10%.
# Вход
# От конзолата се четат 3 реда:
# Ред 1. Бюджет за филма – реално число в интервала [1.00 … 1000000.00]
# Ред 2. Брой на статистите – цяло число в интервала [1 … 500]
# Ред 3. Цена за облекло на един статист – реално число в интервала [1.00 … 1000.00]
# Изход
# На конзолата трябва да се отпечатат два реда:
# · Ако парите за декора и дрехите са повече от бюджета:
# o "Not enough money!"
# o "Wingard needs {парите недостигащи за филма} leva more."
# · Ако парите за декора и дрехите са по малко или равни на бюджета:
# o "Action!"
# o "Wingard starts filming with {останалите пари} leva left."
# Резултатът трябва да е форматиран до втория знак след десетичната запетая.
movie_budjet = float(input())
movie_extra = int(input())
extra_dress_price = float(input())
decoration = movie_budjet * 0.1
if movie_extra > 150 :
    total_price_dress_extra = movie_extra * extra_dress_price * 0.9
else:total_price_dress_extra = movie_extra * extra_dress_price
total_amont = movie_budjet - decoration - total_price_dress_extra
if total_amont >= 0 :
    print("Action!")
    print(f"Wingard starts filming with {total_amont:.2f} leva left.")
else:
    total_amont = abs(total_amont)
    print("Not enough money!")
    print(f"Wingard needs {total_amont:.2f} leva more.")
