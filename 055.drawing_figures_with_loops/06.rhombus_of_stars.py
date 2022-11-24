# Напишете програма, която чете цяло положително число n, въведено от потребителя,
# и печата ромбче от звездички с размер n като в примерите по-долу:
# Примерен вход и изход
# вход	изход		вход	изход		вход	изход		вход	изход
# 1	*
# 2	 *
#   * *
#    *
# 3	  *
#    * *
#   * * *
#    * *
#     *
# 4	   *
#     * *
#    * * *
#   * * * *
#    * * *
#     * *
#      *
n = int(input())
row_calc = n + n - 1
row_print = ''
spaces = ' '
simbol = '*'
simbols_num = 0
for i in range(1,row_calc + 1):
    row_print = ''
    for y in range(1, row_calc + 1):
        if i > n:
            simbols_num = row_calc - i + 1
        else: simbols_num = i
        y > n

        if (i == 1 or i == row_calc) and y == n:
            row_print += simbol
        elif (i == 2 or i == row_calc -1) and ( y == n - 1 or y == n + 1 ):
            row_print += simbol
        elif (i == 3 or i == row_calc -2) and (y == n -2 or y == n or y == n+2):
            row_print += simbol
        else:
            row_print += spaces

    print(row_print)