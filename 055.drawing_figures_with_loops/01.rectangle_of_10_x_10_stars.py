# Напишете програма, която чертае на конзолата правоъгълник от 10 x 10 звездички.
n = 10

for i in range(n):
    row_print = ''
    for y in range(n):
        row_print += "*"
    print(row_print)