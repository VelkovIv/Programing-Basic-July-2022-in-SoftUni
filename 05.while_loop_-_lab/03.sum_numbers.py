# Напишете програма, която чете цяло число от конзолата и на всеки следващ ред цели числа,
# докато тяхната сума стане по-голяма или равна на първоначалното число.
# След приключване на четенето да се отпечата сумата на въведените числа.
number = int(input())
sum_number = 0

while sum_number < number:
    current_number = int(input())
    sum_number += current_number
print(sum_number)