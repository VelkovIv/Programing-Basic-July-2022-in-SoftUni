days = int(input())
hours = int(input())
day_payment = 0
total_payment = 0
for day in range(1, days +1):
    for hour in range(1, hours + 1):
        if day % 2 != 0 and hour % 2 == 0:
            day_payment += 1.25
        elif day % 2 == 0 and hour % 2 != 0:
            day_payment += 2.5
        else :
            day_payment += 1
    print(f"Day: {day} - {day_payment:.2f} leva")
    total_payment += day_payment
    day_payment = 0
print(f"Total: {total_payment:.2f} leva")