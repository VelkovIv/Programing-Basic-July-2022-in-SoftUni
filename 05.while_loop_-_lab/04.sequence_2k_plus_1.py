# Напишете програма, която чете число n, въведено от потребителя, и
# отпечатва всички числа  ≤  n от редицата: 1, 3, 7, 15, 31, ….
# Всяко следващо число се изчислява като умножим предишното с 2 и добавим 1.

number = int(input())
current_num = 1

while current_num <= number :
    print(current_num)
    current_num = 2 * current_num +1