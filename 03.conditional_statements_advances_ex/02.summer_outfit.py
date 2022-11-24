# Лятото е сезон с много променливо време и Виктор има нужда от вашата помощ.
# Напишете програма, която спрямо времето от денонощието и градусите
# да препоръча на Виктор какви дрехи да облече.
# Вашият приятел има различни планове за всеки етап от деня, които изискват и различен външен вид - може да ги видите от таблицата.
# От конзолата се четат точно два реда:
# •	Градусите - цяло число;
# •	Време от денонощието - текст с три възможности "Morning", "Afternoon" или "Evening".
degree = int(input())
day_time = input()
outfit = ""
shoes = ""
if day_time == "Morning":
    if 10 <= degree <= 18 :
        outfit = "Sweatshirt"
        shoes = "Sneakers"
    elif 18 < degree <= 24 :
        outfit = "Shirt"
        shoes = "Moccasins"
    elif degree >= 25 :
        outfit = "T-Shirt"
        shoes = "Sandals"
elif day_time == "Afternoon":
    if 10 <= degree <= 18:
        outfit = "Shirt"
        shoes = "Moccasins"
    elif 18 < degree <= 24:
        outfit = "T-Shirt"
        shoes = "Sandals"
    elif degree >= 25 :
        outfit = "Swim Suit"
        shoes = "Barefoot"
elif day_time == "Evening":
    outfit = "Shirt"
    shoes = "Moccasins"
    # if 10 <= degree <= 18:
    #     outfit = "Shirt"
    #     shoes = "Moccasins"
    # elif 18 < degree <= 24:
    #     outfit = "Shirt"
    #     shoes = "Moccasins"
    # elif degree >= 25:
    #     outfit = "Shirt"
    #     shoes = "Moccasins"
print(f"It's {degree} degrees, get your {outfit} and {shoes}.")