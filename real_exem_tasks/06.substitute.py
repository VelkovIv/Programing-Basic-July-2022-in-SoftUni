k_number = int(input())
l_number = int(input())
m_number = int(input())
n_number = int(input())
change_counter = 0
no_more_changes = False
for first_digit_first_number in range(k_number, 8 + 1):
    if no_more_changes:
        break
    if first_digit_first_number % 2 != 0:
        continue
    for second_digit_first_number in range(9, l_number - 1, - 1):
        if no_more_changes:
            break
        if second_digit_first_number % 2 == 0:
            continue
        for first_digit_second_number in range(m_number, 8 + 1):
            if no_more_changes:
                break
            if first_digit_second_number % 2 != 0:
                continue
            for second_digit_second_number in range(9, n_number - 1, - 1):
                if second_digit_second_number % 2 == 0:
                    continue
                number_first_payer = str(first_digit_first_number)+str(second_digit_first_number)
                number_second_payer = str(first_digit_second_number)+str(second_digit_second_number)
                if number_first_payer == number_second_payer:
                    print("Cannot change the same player.")
                else:
                    print(f"{number_first_payer} - {number_second_payer}")
                    change_counter += 1
                if change_counter == 6:
                    no_more_changes = True
                    break


