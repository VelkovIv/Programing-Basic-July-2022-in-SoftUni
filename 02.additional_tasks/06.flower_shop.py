# •	Магнолии – 3.25 лева
# •	Зюмбюли – 4 лева
# •	Рози – 3.50 лева
# •	Кактуси – 8 лева
# От общата сума, Мария трябва да плати 5% данъци
# Вход
# Входът се чете от конзолата и се състои от 5 реда:
# •	Брой магнолии – цяло число в интервала [0 … 50]
# •	Брой зюмбюли – цяло число в интервала [0 … 50]
# •	Брой рози – цяло число в интервала [0 … 50]
# •	Брой кактуси – цяло число в интервала [0 … 50]
# •	Цена на подаръка – реално число в интервала [0.00 … 500.00]
# Изход
# На конзолата трябва да се отпечата един ред.
# •	Ако парите СА стигнали: "She is left with {останали} leva." – сумата трябва да е закръглена към по-малко цяло число (пр. 1.90 -> 1).
# •	Ако парите НЕ достигат: "She will have to borrow {останали} leva." – сумата трябва да е закръглена към по-голямо цяло число (пр. 1.10 -> 2).
from math import floor, ceil

magnolias_numbers = int(input())
hyacinths_nembers = int(input())
roses_numbers = int(input())
cacti_numbers = int(input())
money_present = float(input())
flowers_price = magnolias_numbers * 3.25 + hyacinths_nembers * 4 + roses_numbers *3.5 + cacti_numbers * 8
total_price = flowers_price * 0.95

if money_present > total_price :
    diff = ceil(money_present - total_price)
    print(f"She will have to borrow {diff} leva.")
else:
    diff = floor(total_price - money_present)
    print(f"She is left with {diff} leva.")