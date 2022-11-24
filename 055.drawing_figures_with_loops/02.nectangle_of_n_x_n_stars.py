# Напишете програма, която чете цяло положително число n, въведено от потребителя, и печата на конзолата правоъгълник от n * n звездички.
n = int(input())

for i in range(n):
    row_print = ''
    for y in range(n):
        row_print += "*"
    print(row_print)