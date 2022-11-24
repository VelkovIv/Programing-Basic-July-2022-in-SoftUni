letter_for_interval_begining = input()
letter_for_interval_ending = input()
letter_for_interval_excluding = input()
combination_counter = 0
begining = ord(letter_for_interval_begining)
ending = ord(letter_for_interval_ending)
excluding = ord(letter_for_interval_excluding)

for first_synbol in range(begining, ending +1):
    if first_synbol == excluding:
        continue
    for second_synbol in range(begining, ending +1):
        if second_synbol == excluding:
            continue
        for third_synbol in range(begining, ending +1):
            if third_synbol == excluding:
                continue
            combination_counter += 1
            print(f"{chr(first_synbol)}{chr(second_synbol)}{chr(third_synbol)}", end = " ")
print(combination_counter)