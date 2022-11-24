# Да се напише програма, която чете 2 * n-на брой цели числа,
# подадени от потребителя, и проверява дали сумата на първите n числа (лява сума)
# е равна на сумата на вторите n числа (дясна сума).
# При равенство печата "Yes, sum = " + сумата; иначе печата "No, diff = " + разликата.
# Разликата се изчислява като положително число (по абсолютна стойност).
n=int(input())
left_sum=0
right_sum=0
iteration = 2*n
for i in range(1,iteration+1):
    number = int(input())
    if n >= i:
        left_sum += + number
    else:
        right_sum += + number
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff=abs(left_sum-right_sum)
    print(f"No, diff = {diff}")