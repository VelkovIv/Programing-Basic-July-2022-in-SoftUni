# Напишете програма, която печата всички числа в интервала от 1 до 100, който се делят на 3 без остатък, по едно на ред.

n = 101
for i in range(1,n):
    if i % 3 ==0:
        print(i)