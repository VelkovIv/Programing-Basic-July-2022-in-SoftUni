# Да се напише програма, която чете число n, въведено от потребителя, и печата триъгълник от долари като в примерите:
n = int(input())
row_print = ''
for i in range(n):

    # for y in range(n):
    row_print += "$ "
    print(row_print)