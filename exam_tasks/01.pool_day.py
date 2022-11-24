from math import ceil

people_number = int(input())
entrance_tax = float(input())
sunbed_price = float(input())
umprela_price = float(input())
if people_number % 2 == 0 :
    total_umbrela_price = people_number / 2 * umprela_price
    total_sunbed_price = ceil(people_number * 0.75) * sunbed_price
else :
    total_umbrela_price = (people_number // 2 + 1) * umprela_price
    total_sunbed_price = ceil(people_number  * 0.75) * sunbed_price
total_price = people_number * entrance_tax + total_umbrela_price + total_sunbed_price
print(f"{total_price:.2f} lv.")
print(total_umbrela_price)
print(total_sunbed_price)

