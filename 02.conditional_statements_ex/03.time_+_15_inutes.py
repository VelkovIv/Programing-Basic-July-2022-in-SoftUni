# 3. Време + 15 минути
# Да се напише програма, която чете час и минути от 24-часово денонощие,
# въведени от потребителя и изчислява колко ще е часът след 15 минути.
# Резултатът да се отпечата във формат часове:минути. Часовете винаги са между 0 и 23,
# а минутите винаги са между 0 и 59. Часовете се изписват с една или две цифри.
# Минутите се изписват винаги с по две цифри, с водеща нула, когато е необходимо.
hour = int(input())
minutes = int(input())
minutes = minutes + 15
if minutes == 60 :
    minutes = 0
    hour = hour + 1
elif minutes > 60 :
    minutes = minutes - 60
    hour = hour + 1
if hour == 24 : hour = 0
if minutes < 10 :
    print(f"{hour}:0{minutes}")
else: print(f"{hour}:{minutes}")
