# Напишете програма, която чете n-на брой числа, въведени от потребителя, и пресмята сумата,
# минимума и максимума на числата на четни и нечетни позиции (броим от 1).
# Когато няма минимален / максимален елемент, отпечатайте "No".
# Изходът да се форматира в следния вид:
# "OddSum=" + {сума на числата на нечетни позиции},
# "OddMin=" + { минимална стойност на числата на нечетни позиции } / {“No”},
# "OddMax=" + { максимална стойност на числата на нечетни позиции } / {“No”},
# "EvenSum=" + { сума на числата на четни позиции },
# "EvenMin=" + { минимална стойност на числата на четни позиции } / {“No”},
# "EvenMax=" + { максимална стойност на числата на четни позиции } / {“No”}
# Всяко число трябва да е форматирано до втория знак след десетичната запетая.
import sys

numbers = int(input())

odd_min = sys.maxsize
odd_max = -sys.maxsize
odd_sum = 0
even_max = -sys.maxsize
even_min = sys.maxsize
even_sum = 0

for i in range(1, numbers + 1, 2):
    current_num_o = float(input())
    odd_sum += current_num_o
    if i == 1:
        odd_min = current_num_o
        odd_max = current_num_o
    elif current_num_o > odd_max :
        odd_max = current_num_o
    elif current_num_o < odd_min :
        odd_min = current_num_o
    if i == numbers :
        break
    for y in range(i+1, i + 2):
        current_num = float(input())
        even_sum += current_num
        if y == 2:
            even_min = current_num
            even_max = current_num
        elif current_num > even_max :
            even_max = current_num
        elif current_num < even_min :
            even_min = current_num


print(f"OddSum={odd_sum:.2f},")

if odd_min == sys.maxsize:
    # odd_min = "No"
    print("OddMin=No,")
else: print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize :
    # odd_max = "No"
    print(f"OddMax=No,")
else:print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    # even_min = "No"
    print(f"EvenMin=No,")
else:print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    # even_max = "No"
    print(f"EvenMax=No")
else:print(f"EvenMax={even_max:.2f}")