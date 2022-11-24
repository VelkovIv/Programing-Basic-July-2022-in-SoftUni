# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя,
# намира най-малкото измежду тях и го принтира. Въвежда се по едно число на ред.
import sys

min_num = sys.maxsize

while True:
    current_num = input()
    if current_num == 'Stop':
        break
    current_num = int(current_num)
    if current_num < min_num:
        min_num = current_num

print(min_num)