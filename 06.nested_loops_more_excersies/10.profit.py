one_lv_coins = int(input())
two_lv_coins = int(input())
five_lv_banknote = int(input())
amount = int(input())


for one in range(one_lv_coins + 1):
    for two in range(two_lv_coins + 1):
        for five in range(five_lv_banknote + 1):
            if one * 1 + two * 2 + five * 5 == amount:
                print(f"{one} * 1 lv. + {two} * 2 lv. + {five} * 5 lv. = {amount} lv.")

