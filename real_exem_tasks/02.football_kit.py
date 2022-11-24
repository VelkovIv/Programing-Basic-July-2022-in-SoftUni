t_short_price = float(input())
amount_to_will_ball = float(input())

shorts_price = t_short_price * 0.75
socks_price = shorts_price * 0.2
shues = (t_short_price + shorts_price) * 2
total_amount = (t_short_price + shorts_price + socks_price + shues) * 0.85
if total_amount >= amount_to_will_ball:
    print("Yes, he will earn the world-cup replica ball!")
    print(f"His sum is {total_amount:.2f} lv.")
else:
    print("No, he will not earn the world-cup replica ball.")
    diff = abs(amount_to_will_ball - total_amount)
    print(f"He needs {diff:.2f} lv. more.")