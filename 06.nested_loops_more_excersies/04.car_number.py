first_number = int(input())
second_number = int(input())

for first_digit in range(first_number, second_number +1 ):
    for second_digit in range(first_number, second_number +1 ):
        for third_digit in range(first_number, second_number +1 ):
            if (second_digit + third_digit) % 2 !=0:
                continue
            for fourth_digit in range(first_number, second_number +1 ):
                if first_digit > fourth_digit :
                    if (first_digit % 2 == 0 and fourth_digit % 2 != 0) :#or (first_digit % 2 != 0 and fourth_digit % 2 == 0) :
                        print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end = " ")
                    elif (first_digit % 2 != 0 and fourth_digit % 2 == 0) :
                        print(f"{first_digit}{second_digit}{third_digit}{fourth_digit}", end = " ")