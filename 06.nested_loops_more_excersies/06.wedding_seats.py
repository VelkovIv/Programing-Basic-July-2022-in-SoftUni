last_sector_letter = input()
row_number_first_sector = int(input())
seats_number_odd_row = int(input())
first_sector_number = 65
last_sector_number = ord(last_sector_letter)
row_number = row_number_first_sector - 1
seat_counter = 0
for sector in range(first_sector_number, last_sector_number + 1):
    row_number += 1
    for row in range(1,row_number + 1):
        for seat in range(1, seats_number_odd_row + 3):
            real_seat = chr(seat + 96)
            real_sector = chr(sector)

            print(f"{real_sector}{row}{real_seat}")
            seat_counter += 1
            if row % 2 != 0 and seat == seats_number_odd_row:
                break
print(seat_counter)