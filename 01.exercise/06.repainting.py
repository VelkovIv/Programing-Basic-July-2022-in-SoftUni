nylon_m2 = int(input())
paint_lt = int(input())
thinner_lt = int(input())
work_hours = int(input())
mat_price = (nylon_m2 +2) * 1.5 + paint_lt * 1.1 * 14.5 + thinner_lt * 5 + 0.4
work_price = mat_price * 0.3 * work_hours
total_price = mat_price + work_price
print(total_price)