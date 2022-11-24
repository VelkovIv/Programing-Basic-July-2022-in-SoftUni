# Напишете програма, която прочита едно число n, след това прочита n на брой цели числа и принтира
# средно аритметичното на тяхната сума число, форматирано до втората цифра след десетични знак.

number = int(input())
sum = 0
counter = 0

for i in range(1, number + 1):
    current_num = int(input())
    sum += current_num
average = sum / number
print(f"{average:.2f}")