processor_price_usd = float(input())
video_card_price_usd = float(input())
ram_price_usd = float(input())
ram_numbers = int(input())
precent_discount = float(input())

processor_price_bgn = processor_price_usd * 1.57
video_card_price_bgn = video_card_price_usd * 1.57
ram_price_bgn = ram_price_usd * 1.57
total_pricessor_price_bgn = processor_price_bgn * (1 - precent_discount)
total_video_card_price_bgn = video_card_price_bgn * (1 - precent_discount)
tatal_ram_price = ram_price_bgn * ram_numbers
total_amont = total_pricessor_price_bgn + total_video_card_price_bgn + tatal_ram_price

print(f"Money needed - {total_amont:.2f} leva.")