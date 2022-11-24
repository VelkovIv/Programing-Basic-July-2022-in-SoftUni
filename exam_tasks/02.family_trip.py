# Семейство Иванови планират семейната си почивка.
# Вашата задача е да напишете програма, която да изчислява дали предвидения от тях бюджет ще им стигне,
# като знаете колко нощувки са планирали, каква е цената за нощувка и колко процента от бюджета са предвидили за допълнителни разходи.
# Трябва да се има предвид, че ако броят на нощувките е по-голям от 7, цената за нощувка се намаля с 5%.
# Вход
# От конзолата се четат 4 реда:
# · Бюджетът, с който разполагат – реално число в интервала [1.00 … 10000.00]
# · Брой нощувки – цяло число в интервала [0 … 1000]
# · Цена за нощувка – реално число в интервала [1.00 … 500.00]
# · Процент за допълнителни разходи – цяло число в интервала [0 … 100]
# Изход
# Отпечатването на конзолата зависи от резултата:
# · Ако сумата е достатъчна:
# o "Ivanovi will be left with {останали пари след почивката} leva after vacation."
# · Ако НЕ е достигната сумата:
# o "{парите нужни до достигане на целта} leva needed."
# Сума трябва да се форматира до втората цифра след десетичния знак

budjet = float(input())
nights_number = int(input())
night_price = float(input())
additional_expences_per = int(input())
if nights_number > 7 :
    night_price = night_price * 0.95
family_vacation_price = nights_number * night_price
additional_expences = budjet * additional_expences_per / 100
final_price = family_vacation_price + additional_expences
remainning_money = abs(budjet - final_price)
if budjet >= final_price:
    print(f"Ivanovi will be left with {remainning_money:.2f} leva after vacation.")
else:print(f"{remainning_money:.2f} leva needed.")
