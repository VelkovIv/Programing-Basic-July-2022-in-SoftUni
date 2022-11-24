joinery_numbers = int(input())
joinery_type = input()
delivery = input()
price = 0
total_price = 0
discount = 1
if joinery_type == "90X130":
    price = 110
    if joinery_numbers > 60:
        discount = 0.92
    elif joinery_numbers > 30:
        discount = 0.95
elif joinery_type == "100X150":
    price = 140
    if joinery_numbers > 80:
        discount = 0.90
    elif joinery_numbers > 40:
        discount = 0.94
elif joinery_type == "130X180":
    price = 190
    if joinery_numbers > 50:
        discount = 0.88
    elif joinery_numbers > 20:
        discount = 0.93
elif joinery_type == "200X300":
    price = 250
    if joinery_numbers > 50:
        discount = 0.86
    elif joinery_numbers > 25:
        discount = 0.91

if delivery == "Without delivery":
    delivery = 0
else:
    delivery = 60
total_price = price * joinery_numbers * discount + delivery

if joinery_numbers > 99:
    total_price *= 0.96

if joinery_numbers < 10:
    print("Invalid order")
else:
    print(f"{total_price:.2f} BGN")
