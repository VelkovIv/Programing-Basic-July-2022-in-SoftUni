# В една кинозала столовете са наредени в правоъгълна форма в r реда и c колони.
# Има три вида прожекции с билети на различни цени:
# •	Premiere - премиерна прожекция, на цена 12.00 лева;
# •	Normal - стандартна прожекция, на цена 7.50 лева;
# •	Discount - прожекция за деца, ученици и студенти на намалена цена от 5.00 лева.
# Напишете програма, която чете тип прожекция (текст), брой редове и брой колони в залата (цели числа),
# въведени от потребителя, и изчислява общите приходи от билети при пълна зала.
# Резултатът да се отпечата във формат 2 знака след десетичната точка.

screening_type = input()
rows_number = int(input())
columns_number = int(input())
seats_numers = rows_number * columns_number
ticket_price = 0
if screening_type == "Premiere":
    ticket_price= 12.00
elif screening_type == "Normal":
    ticket_price = 7.50
elif screening_type == "Discount":
    ticket_price = 5.00
total_tickets_price = rows_number * columns_number * ticket_price
print(f"{total_tickets_price:.2f}")

