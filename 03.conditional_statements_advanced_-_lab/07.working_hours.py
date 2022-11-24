# Да се напише програма, която чете час от денонощието(цяло число) и ден от седмицата(текст) -
# въведени от потребителя и проверява дали офисът на фирма е отворен,
# като работното време на офисът е от 10-18 часа, от понеделник до събота включително

hour_of_the_day =int(input())
day_of_the_week = input()
if 10 <= hour_of_the_day <= 18:
    if day_of_the_week == "Monday" \
        or day_of_the_week == "Tuesday" \
        or day_of_the_week == "Wednesday" \
        or day_of_the_week == "Thursday" \
        or day_of_the_week == "Friday" \
        or day_of_the_week == "Saturday":
        print("open")
    else: print("closed")
else: print("closed")