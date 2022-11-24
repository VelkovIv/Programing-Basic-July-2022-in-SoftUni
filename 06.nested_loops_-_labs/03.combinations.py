# Напишете програма, която изчислява колко решения в естествените числа (включително и нулата) има уравнението:
# x1 + x2 + x3 = n
# Числото n е цяло число и се въвежда от конзолата.
num = int(input())
combination_count = 0
for x1 in range(num+1):
    for x2 in range(num+1):
        for x3 in range(num+1):
            if x1 + x2 + x3 == num :
                combination_count +=1
print(combination_count)