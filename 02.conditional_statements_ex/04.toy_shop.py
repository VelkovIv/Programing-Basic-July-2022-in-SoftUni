# Петя има магазин за детски играчки. Тя получава голяма поръчка, която трябва да изпълни.
# С парите, които ще спечели иска да отиде на екскурзия.
# Цени на играчките:
# · Пъзел - 2.60 лв.
# · Говореща кукла - 3 лв.
# · Плюшено мече - 4.10 лв.
# · Миньон - 8.20 лв.
# · Камионче - 2 лв.
# Ако поръчаните играчки са 50 или повече магазинът прави отстъпка 25% от общата цена.
# От спечелените пари Петя трябва да даде 10% за наема на магазина. Да се пресметне дали парите ще ѝ стигнат да отиде на екскурзия.
# Вход
# От конзолата се четат 6 реда:
# 1. Цена на екскурзията - реално число в интервала [1.00 … 10000.00]
# 2. Брой пъзели - цяло число в интервала [0… 1000]
# 3. Брой говорещи кукли - цяло число в интервала [0 … 1000]
# 4. Брой плюшени мечета - цяло число в интервала [0 … 1000]
# 5. Брой миньони - цяло число в интервала [0 … 1000]
# 6. Брой камиончета - цяло число в интервала [0 … 1000]
# Изход
# На конзолата се отпечатва:
# · Ако парите са достатъчни се отпечатва:
# o "Yes! {оставащите пари} lv left."
# · Ако парите НЕ са достатъчни се отпечатва:
# o "Not enough money! {недостигащите пари} lv needed."
# Резултатът трябва да се форматира до втория знак след десетичната запетая.
trip_price = float(input())
number_puzzels = int(input())
number_talking_dolls = int(input())
number_bears = int(input())
number_minions = int(input())
number_trucks = int(input())
total_toys = number_puzzels + number_talking_dolls + number_bears + number_minions + number_trucks

puzzels_price = number_puzzels * 2.6
talking_dolls_price = number_talking_dolls * 3
bears_price = number_bears * 4.1
minions_price = number_minions * 8.2
truck_price = number_trucks * 2
total_price = puzzels_price + talking_dolls_price + bears_price + minions_price + truck_price

if total_toys >= 50 :
    final_price = total_price * 0.75 * 0.9
else: final_price = total_price * 0.9

if final_price >= trip_price :
    remain = final_price - trip_price
    print(f"Yes! {remain:.2f} lv left.")
else:
    remain = trip_price - final_price
    print(f"Not enough money! {remain:.2f} lv needed.")
