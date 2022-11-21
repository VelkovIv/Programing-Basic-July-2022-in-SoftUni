# Напишете програма, която при въведени градуси (реално число) принтира какво е времето, като имате предвид следната таблица:
# Градуси	Време
# 26.00 - 35.00	Hot
# 20.1 - 25.9	Warm
# 15.00 - 20.00	Mild
# 12.00 - 14.9	Cool
# 5.00 - 11.9	Cold
degree = float(input())

if degree <5 :
    print("unknown")
elif degree <= 11.9 :
    print("Cold")
elif degree <= 14.9:
    print("Cool")
elif degree <= 20:
    print("Mild")
elif degree <= 25.9:
    print("Warm")
elif degree <= 35:
    print("Hot")
else: print("unknown")