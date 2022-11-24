day_target = int(input())
customer_price = 0
earned_money = 0
command = input()
is_target_reach = False
while command != "closed" :
    survice_type = command
    detail_type = input()
    if survice_type == "haircut":
        if detail_type == "mens":
            customer_price = 15
        elif detail_type == "ladies":
            customer_price = 20
        elif detail_type == "kids":
            customer_price = 10
    elif survice_type == "color":
        if detail_type == "touch up":
            customer_price = 20
        elif detail_type == "full color":
            customer_price = 30
    earned_money += customer_price
    if earned_money >= day_target :
        is_target_reach = True
        break

    command = input()
if is_target_reach:
    print("You have reached your target for the day!")
else:
    diff = abs(day_target - earned_money)
    print(f"Target not reached! You need {diff}lv. more.")
print(f"Earned money: {earned_money}lv.")
