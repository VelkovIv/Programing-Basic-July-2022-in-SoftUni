# Да се напише програма която чете ден от седмицата (текст) –
# въведен от потребителя и принтира на конзолата цената на билет за кино според деня от седмицата:
# Monday	Tuesday	Wednesday	Thursday	Friday	Saturday	Sunday
# 12	12	14	14	12	16	16
day_of_the_week = input()
if day_of_the_week == "Monday" \
    or day_of_the_week == "Tuesday" \
    or day_of_the_week == "Friday" :
    print(12)
elif day_of_the_week == "Wednesday" \
    or day_of_the_week == "Thursday" :
    print(14)
elif day_of_the_week == "Saturday" \
    or day_of_the_week == "Sunday" :
    print(16)