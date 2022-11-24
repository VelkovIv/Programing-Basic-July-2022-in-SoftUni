first_number = input()
second_number = input()
first_number_beggining = int(first_number[0])
second_number_beggining = int(first_number[1])
third_number_beggining = int(first_number[2])
fourd_number_beggining = int(first_number[3])
first_number_ending = int(second_number[0])
second_number_ending = int(second_number[1])
third_number_ending = int(second_number[2])
fourd_number_ending = int(second_number[3])

for one in range(first_number_beggining,first_number_ending + 1):
    if one % 2 ==0:
        continue
    for two in range(second_number_beggining, second_number_ending + 1):
        if two % 2 == 0:
            continue
        for three in range(third_number_beggining, third_number_ending + 1):
            if three % 2 == 0:
                continue
            for four in range(fourd_number_beggining, fourd_number_ending + 1):
                if four % 2 ==0:
                    continue
                print(f"{one}{two}{three}{four}", end=" ")
