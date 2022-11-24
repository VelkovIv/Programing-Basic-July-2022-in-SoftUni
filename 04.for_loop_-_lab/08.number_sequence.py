# Напишете програма, която чете n на брой цели числа. Принтирайте най-голямото и най-малкото число сред въведените.
import sys

numbers_for_loop = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(1,numbers_for_loop+1):
    number=int(input())
    if number <= min_number:
        min_number = number
    if number >= max_number:
        max_number = number

print(f"Max number: {max_number}")
print(f"Min number: {min_number}")
