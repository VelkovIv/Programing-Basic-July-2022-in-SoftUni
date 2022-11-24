cinema_capacity = int(input())
command = input()
ticket_price = 0
sold_tickets = 0
is_full = False
while command != "Movie time!":
    current_people = int(command)
    sold_tickets += current_people
    if sold_tickets > cinema_capacity:
        is_full = True
        break
    if current_people % 3 ==0:
        ticket_price += current_people * 5 - 5
    else:
        ticket_price += current_people * 5
    command = input()
if is_full:
    print("The cinema is full.")
else:
    left_seat = cinema_capacity - sold_tickets
    print(f"There are {left_seat} seats left in the cinema.")
print(f"Cinema income - {ticket_price:.0f} lv.")
