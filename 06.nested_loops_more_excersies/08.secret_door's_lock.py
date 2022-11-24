upper_border_hundreds_digit = int(input())
upper_border_tens_digit = int(input())
upper_border_ones_digit = int(input())
if upper_border_tens_digit > 7:
    upper_border_tens_digit = 7
for hundreds_digit in range(1, upper_border_hundreds_digit + 1):
    if hundreds_digit % 2 != 0:
        continue
    for tens_digit in range(2, upper_border_tens_digit + 1):
        if tens_digit >2 and tens_digit % 2 == 0:
            continue
        for ones_digit in range(1, upper_border_ones_digit + 1):
            if ones_digit % 2 != 0:
                continue
            print(f"{hundreds_digit} {tens_digit} {ones_digit}")