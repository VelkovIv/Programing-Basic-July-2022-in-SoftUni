# Когато пуснали билетите за Евро 2016, група запалянковци решили да си закупят.
# Билетите имат две категории с различни цени:
# •	IP – 499.99 лева.
# •	Normal – 249.99 лева.
# Запалянковците имат определен бюджет, а броят на хората в групата определя какъв процент от бюджета трябва да се задели за транспорт
# •	От 1 до 4 – 75% от бюджета.
# •	От 5 до 9 – 60% от бюджета.
# •	От 10 до 24 – 50% от бюджета.
# •	От 25 до 49 – 40% от бюджета.
# •	50 или повече – 25% от бюджета.
# Напишете програма, която да пресмята дали с останалите пари от бюджета могат да си купят билети за избраната категория.
# И колко пари ще им останат или ще са им нужни.
# Вход
# Входът се чете от конзолата и съдържа точно 3 реда:
# •	На първия ред е бюджетът – реално число в интервала [1 000.00 ... 1 000 000.00]
# •	На втория ред е категорията – "VIP" или "Normal"
# •	На третия ред е броят на хората в групата – цяло число в интервала [1 ... 200]
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако бюджетът е достатъчен:
# o	"Yes! You have {останалите пари на групата} leva left."
# •	Ако бюджетът НЕ Е достатъчен:
# o	"Not enough money! You need {сумата, която не достига} leva."
# Сумите трябва да са форматирани с точност до два знака след десетичната запетая.
budget = float(input())
ticket_type = input()
number_of_people = int(input())

travel_expemces = 0
if 1 <= number_of_people < 5 :
    travel_expemces = budget * 0.75
elif 5 <= number_of_people < 10:
    travel_expemces = budget * 0.60
elif 10 <= number_of_people < 25:
    travel_expemces = budget * 0.50
elif 25 <= number_of_people < 50:
    travel_expemces = budget * 0.40
else: travel_expemces = budget * 0.25
money_for_tickets = budget - travel_expemces

if ticket_type == "Normal" :
    tickets_money = number_of_people * 249.99
else:
    tickets_money = number_of_people * 499.99
diff = abs(money_for_tickets - tickets_money)

if money_for_tickets >= tickets_money :
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
