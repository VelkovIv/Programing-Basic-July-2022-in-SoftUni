men_number = int(input())
women_number = int(input())
tables_number = int(input())
is_table_finish = False
for man in range(1, men_number + 1):
    for woman in range(1, women_number + 1):
        if tables_number <= 0:
            is_table_finish = True
            break
        print(f"({man} <-> {woman})", end =" ")
        tables_number -=1
    if is_table_finish:
        break