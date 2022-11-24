# Напишете програма, която до получаване на командата "Stop", чете цели числа, въведени от потребителя, =
# намира най-голямото измежду тях и го принтира. Въвежда се по едно число на ред.
import sys

max_num = -sys.maxsize

while True:
    current_num = input()
    if current_num == 'Stop':
        break
    current_num = int(current_num)
    if current_num > max_num:
        max_num = current_num

print(max_num)