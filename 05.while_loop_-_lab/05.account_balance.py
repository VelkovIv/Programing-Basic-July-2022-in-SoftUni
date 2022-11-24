# Напишете програма, която пресмята колко общо пари има в сметката, след като направите определен брой вноски.
# На всеки ред ще получавате сумата, която трябва да внесете в сметката, до получаване на команда  "NoMoreMoney ".
# При всяка получена сума на конзолата трябва да се извежда "Increase: " + сумата и тя да се прибавя в сметката.
# Ако получите число по-малко от 0 на конзолата трябва да се изведе "Invalid operation!"  и програмата да приключи.
# Когато програмата приключи трябва да се принтира "Total: " + общата сума в сметката форматирана до втория знак след десетичната запетая.
total_sum = 0
while True:
    current_amount = input()
    if current_amount == 'NoMoreMoney':
        break
    current_amount = float(current_amount)
    if current_amount < 0:
        print("Invalid operation!")
        break
    else:
        print(f"Increase: {current_amount:.2f}")
    total_sum += current_amount
print(f"Total: {total_sum:.2f}")