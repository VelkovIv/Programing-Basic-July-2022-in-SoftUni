# 	"room for one person" – 18.00 лв за нощувка
# 	"apartment" – 25.00 лв за нощувка
# 	"president apartment" – 35.00 лв за нощувка
# Според броят на дните, в които ще остане в хотела
# (пример: 11 дни = 10 нощувки) и видът на помещението, което ще избере, той може да ползва различно намаление.
# Намаленията са както следва:
# вид помещение	            по-малко от 10 дни	    между 10 и 15 дни	    повече от 15 дни
# room for one person	    не ползва намаление	    не ползва намаление	    не ползва намаление
# apartment	                30% от крайната цена	35% от крайната цена	50% от крайната цена
# president apartment	    10% от крайната цена	15% от крайната цена	20% от крайната цена
# След престоя, оценката на Атанас за услугите на хотела може да е позитивна (positive) или негативна (negative) .
# Ако оценката му е позитивна, към цената с вече приспаднатото намаление Атанас добавя 25% от нея.
# Ако оценката му е негативна приспада от цената 10%.
# Вход
# Входът се чете от конзолата и се състои от три реда:
# •	Първи ред - дни за престой - цяло число в интервала [0...365]
# •	Втори ред - вид помещение - "room for one person", "apartment" или "president apartment"
# •	Трети ред - оценка - "positive"  или "negative"
# Изход
# На конзолата трябва да се отпечата един ред:
# •	Цената за престоят му в хотела, форматирана до втория знак след десетичната запетая.
vacation_days = int(input())
room_type = input()
feedback = input()
night_for_payment = vacation_days - 1
vacation_price = 0
if room_type == "room for one person" :
    vacation_price = night_for_payment * 18.00
elif room_type == "apartment" :
    vacation_price = night_for_payment * 25.00
    if night_for_payment < 10 :
        vacation_price = vacation_price * 0.7
    elif night_for_payment > 15 :
        vacation_price = vacation_price * 0.5
    else:
        vacation_price = vacation_price * 0.65
elif room_type == "president apartment" :
    vacation_price = night_for_payment * 35.00
    if night_for_payment < 10 :
        vacation_price = vacation_price * 0.9
    elif night_for_payment > 15 :
        vacation_price = vacation_price * 0.8
    else:
        vacation_price = vacation_price * 0.85
if feedback == "positive" :
    vacation_price = vacation_price * 1.25
else:
    vacation_price = vacation_price * 0.9
print(f"{vacation_price:.2f}")

