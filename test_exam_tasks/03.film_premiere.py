movie_name = input()
package = input()
ticket_number = int(input())
discount = 1

if movie_name == "John Wick":
    if package == "Drink":
        package = 12
    elif package == "Popcorn":
        package = 15
    else: package = 19
elif movie_name == "Star Wars":
    if package == "Drink":
        package = 18
    elif package == "Popcorn":
        package = 25
    else: package = 30
    if ticket_number >= 4:
        discount = 0.7
else:
    if package == "Drink":
        package = 9
    elif package == "Popcorn":
        package = 11
    else: package = 14
    if ticket_number == 2:
        discount = 0.85
total_price = package * ticket_number * discount
print(f"Your bill is {total_price:.2f} leva.")