# Дадени са 2*n-на брой числа. Първото и второто формират двойка, третото и четвъртото също и т.н.
# Всяка двойка има стойност – сумата от съставящите я числа.
# Напишете програма, която проверява дали всички двойки имат еднаква стойност или печата максималната разлика
# между две последователни двойки.
# Ако всички двойки имат еднаква стойност, отпечатайте "Yes, value={Value}" + стойността.
# В противен случай отпечатайте "No, maxdiff={Difference}" + максималната разлика.
import sys

nums = int(input())
nums = 2 * nums

max_sum = -sys.maxsize
min_sum = sys.maxsize
current_sum = 0
step = 0
for i in range(1, nums+1):
    current_num = int(input())
    current_sum += current_num
    if i % 2 == 0 :
        if current_sum > max_sum :
            if max_sum == -sys.maxsize:
                 min_sum = current_sum
            max_sum = current_sum
            current_sum = 0
        else:
            min_sum = current_sum
            current_sum = 0

if min_sum == sys.maxsize:
    min_sum = max_sum

if min_sum == max_sum :
    print(f"Yes, value={max_sum}")
else:
    diff = abs(max_sum - min_sum)
    print(f"No, maxdiff={diff}")