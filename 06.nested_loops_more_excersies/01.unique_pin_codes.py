upper_border_first_digit = int(input())
upper_border_second_digit = int(input())
upper_border_third_digit = int(input())
if upper_border_first_digit % 2 != 0:
    upper_border_first_digit -= 1
if upper_border_second_digit > 7:
    upper_border_second_digit = 7
if upper_border_third_digit % 2 != 0:
    upper_border_third_digit -=1
is_print = True

for first_digit in range(2, upper_border_first_digit +1 ,2):
    for second_digit in range(2, upper_border_second_digit + 1):
        if second_digit > 2 :
            if second_digit % 2 == 0:
                continue
            # elif second_digit % 3 == 0 :
            #     continue
        for third_digit in range(2, upper_border_third_digit + 1, 2):
            print(f"{first_digit} {second_digit} {third_digit}")
