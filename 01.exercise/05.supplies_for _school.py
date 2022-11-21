pens_packaging = int(input())
markers_packaging = int(input())
cleaner_lt = int(input())
discout = int(input())

price_pens = pens_packaging * 5.8
price_markers = markers_packaging * 7.2
price_cleaner = cleaner_lt * 1.2
total_price = price_pens + price_markers + price_cleaner
finale_price = total_price * (1 - discout/100)
print(finale_price)
