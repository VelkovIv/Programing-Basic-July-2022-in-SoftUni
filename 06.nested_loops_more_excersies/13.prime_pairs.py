first_couple_begin = int(input())
second_couple_begin = int(input())
first_end = int(input())
second_end = int(input())
first_couple_end = first_couple_begin + first_end
second_couple_end = second_couple_begin + second_end

for couple_one in range(first_couple_begin, first_couple_end + 1):
    for couple_two in range(second_couple_begin, second_couple_end + 1):
        if couple_one % 2 != 0 and couple_one % 3 !=0 and couple_one % 5 !=0 and couple_one % 7 !=0 \
                and couple_two % 2 != 0 and couple_two % 3 != 0 and couple_two % 5 !=0 and couple_two % 7 !=0:
            print(f"{couple_one}{couple_two}")