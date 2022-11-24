number = int(input())
current = 1
is_n_bigger_than_current = False
for row in range(1, number + 1):
    for col in range(1, row + 1):
        if current > number :
            is_n_bigger_than_current = True
            break
        print(str(current) + " ", end = '')
        current += 1
    if is_n_bigger_than_current :
        break
    print()