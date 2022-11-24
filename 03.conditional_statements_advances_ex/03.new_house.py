flower_type = input()
number_of_flowers = int(input())
budget = int(input())

discount = 0
if flower_type == "Roses":
    if number_of_flowers > 80 :
        discount = 0.9
        bill = number_of_flowers * 5 * discount
    else: bill = number_of_flowers * 5
elif flower_type == "Dahlias":
    if number_of_flowers > 90:
        discount = 0.85
        bill = number_of_flowers * 3.8 * discount
    else:
        bill = number_of_flowers * 3.8
elif flower_type == "Tulips":
    if number_of_flowers > 80:
        discount = 0.85
        bill = number_of_flowers * 2.8 * discount
    else:
        bill = number_of_flowers * 2.8
elif flower_type == "Narcissus":
    if number_of_flowers < 120:
        discount = 1.15
        bill = number_of_flowers * 3 * discount
    else:
        bill = number_of_flowers * 3
elif flower_type == "Gladiolus":
    if number_of_flowers < 80:
        discount = 1.2
        bill = number_of_flowers * 2.5 * discount
    else:
        bill = number_of_flowers * 2.5
remaining_amount = abs(budget - bill)
if budget >= bill:
    print(f"Hey, you have a great garden with {number_of_flowers} {flower_type} and {remaining_amount:.2f} leva left.")
else:
    print(f"Not enough money, you need {remaining_amount:.2f} leva more.")