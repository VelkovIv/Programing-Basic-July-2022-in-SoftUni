vegi_kilo_price = float(input())
fruit_kilo_price = float(input())
total_vegi_kilo = float(input())
total_fruit_kilo = float(input())
price_vegi = vegi_kilo_price * total_vegi_kilo
price_friut = fruit_kilo_price * total_fruit_kilo
total_bgn_price = price_vegi + price_friut
price_euro = total_bgn_price / 1.94

print(f"{price_euro:.2f}")

