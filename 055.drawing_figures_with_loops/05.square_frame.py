# Напишете програма, която чете цяло положително число n, въведено от потребителя, и чертае на конзолата
# квадратна рамка с размер n * n като в примерите по-долу:
# Примерен вход и изход
# вход	изход		вход	изход		вход	изход		вход	изход
# 3	  + - +
#     | - |
#     + - +
# 4	+ - - +
#     | - - |
#     | - - |
#     + - - +
# 5   + - - - +
#     | - - - |
#     | - - - |
#     | - - - |
#     + - - - +
# 6	   + - - - - +
#     | - - - - |
#     | - - - - |
#     | - - - - |
#     | - - - - |
#     + - - - - +
n = int(input())
first_row = 0

for i in range(1,n + 1):
    row_print = ''
    for y in range(1, n + 1):
        if i == 1 and y == 1:
            row_print += "+ "
        elif i == 1 and y == n:
            row_print += "+ "
        elif i == n and y == 1 :
            row_print += "+ "
        elif i == n and y == n:
            row_print += "+ "
        elif i > 1 and y == 1:
            row_print += "| "
        elif i > 1 and y == n:
            row_print += "| "
        else:
            row_print += "- "

    print(row_print)