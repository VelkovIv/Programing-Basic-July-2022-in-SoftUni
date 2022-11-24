# Да се напише програма, която чете n-на брой цели числа, въведени от потребителя,и проверява
# дали сред тях съществува число, което е равно на сумата на всички останали.
# •	Ако има такъв елемент печата "Yes" и на нов ред "Sum = "  + неговата стойност
# •	Ако няма такъв елемент печата "No" и на нов ред "Diff = " + разликата между най-големия елемент
# и сумата на останалите (по абсолютна стойност)
import sys

n = int(input())

total_sum = 0
max_number = -sys.maxsize

for i in range(1,n+1):
    number = int(input())
    if number>max_number:
        max_number = number
    total_sum += number
if max_number == total_sum - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    total_sum = total_sum - max_number
    diff = abs(total_sum - max_number)
    print("No")
    print(f"Diff = {diff}")
