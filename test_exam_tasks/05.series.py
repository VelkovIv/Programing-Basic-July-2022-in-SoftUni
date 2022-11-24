budget = float(input())
tv_show_numbers = int(input())

for number in range(1, tv_show_numbers + 1):
    tv_show_name = input()
    tv_show_price = float(input())
    discount = 1
    if tv_show_name == "Thrones":
        discount = 0.5
    elif tv_show_name == "Lucifer":
        discount = 0.6
    elif tv_show_name == "Protector":
        discount = 0.7
    elif tv_show_name == "TotalDrama":
        discount = 0.8
    elif tv_show_name == "Area":
        discount = 0.9
    tv_show_price = tv_show_price * discount
    budget -= tv_show_price

if budget >= 0:
    print(f"You bought all the series and left with {budget:.2f} lv.")
else:
    budget = abs(budget)
    print(f"You need {budget:.2f} lv. more to buy the series!")