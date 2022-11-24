first_number = int(input())
second_number = int(input())
max_pass_number = int(input())
first_symbol= 35
second_symbol = 64

is_all_pass_generated = False
for first_digit in range(1, first_number + 1):
    for second_digit in range(1, second_number +1):
        if first_symbol > 55:
            first_symbol = 35
        if second_symbol > 96:
            second_symbol = 64
        symbol_one = chr(first_symbol)
        symbol_two = chr(second_symbol)
        print(f"{symbol_one}{symbol_two}{first_digit}{second_digit}{symbol_two}{symbol_one}", end = "|")
        max_pass_number -= 1
        if max_pass_number <= 0:
            is_all_pass_generated = True
            break
        first_symbol += 1
        second_symbol += 1
    if is_all_pass_generated:
        break
