# Да се напише програма, която чете едно цяло число N, въведено от потребителя,
# и генерира всички възможни "специални" числа от 1111 до 9999.
# За да бъде “специално” едно число, то трябва да отговаря на следното условие:
# •	N да се дели на всяка една от неговите цифри без остатък.
# Пример: при N = 16, 2418 е специално число:
# •	16 / 2 = 8 без остатък
# •	16 / 4 = 4 без остатък
# •	16 / 1 = 16 без остатък
# •	16 / 8 = 2 без остатък

number = int(input())

for current_number in range(1111, 10000):
    current_number = str(current_number)
    is_special = True
    for digit in current_number:
        if int(digit) == 0 or number % int(digit) !=0:
            is_special = False
            break
    if is_special :
        print(current_number, end = " ")