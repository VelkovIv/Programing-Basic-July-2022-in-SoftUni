dancers = int(input())
point_numbers = float(input())
season = input()
place = input()

money = dancers * point_numbers
if place == "Abroad":
    money += money/2

if season == "summer":
    if place == "Bulgaria":
        money *= 0.95
    elif place == "Abroad":
        money *= 0.9
elif season == "winter":
    if place == "Bulgaria":
        money *= 0.92
    elif place == "Abroad":
        money *= 0.85
charity_amount = money * 0.75
money_per_dancer = (money - charity_amount) / dancers
print(f"Charity - {charity_amount:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")