# Напишете програма, която чете цяло число, въведено от потребителя, и отпечатва ден от седмицата(
# на английски език), в граници [1...7] или отпечатва "Error" в случай, че въведеното число е невалидно.

day_of_the_week = int(input())
if day_of_the_week == 1 :
    print("Monday")
elif day_of_the_week == 2 :
    print("Teusday")
elif day_of_the_week == 3 :
    print("Wednessday")
elif day_of_the_week == 4:
    print("Thursday")
elif day_of_the_week == 5 :
    print("Friday")
elif day_of_the_week == 6 :
    print("Saturday")
elif day_of_the_week == 7 :
    print("Sunday")
else: print("Error")

