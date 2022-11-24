# Частно училище организира лагери за учениците по време на ваканциите.
# В зависимост от вида на ваканцията (пролетна, лятна или зимна) и вида на групата (момчета/момичета или смесена)
# цената на нощувката в хотела е различна, както и спортът, който ще практикуват учениците.
# 	                Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момчета/момичета	9.60	        7.20	            15
# смесена група	    10	            9.50	            20
# Училището получава отстъпка от крайната цена, в зависимост от броя на настанените в хотела ученици:
# •	Ако броят на учениците е 50 или повече, училището получава 50% отстъпка
# •	Ако броят на учениците е 20 или повече и в същото време по-малък от 50, училището получава 15% отстъпка
# •	Ако броят на учениците е 10 или повече и в същото време по-малък от 20, училището получава 5% отстъпка
# В таблицата по-долу са дадени спортовете, които ще се практикуват в зависимост от вида на ваканцията и групата:
# 	                Зимна ваканция	Пролетна ваканция	Лятна ваканция
# момичета	        Gymnastics	    Athletics	        Volleyball
# момчета	        Judo	        Tennis	            Football
# смесена група	    Ski	            Cycling	            Swimming
# Да се напише програма, която пресмята цената, която ще заплати училището за нощувките и принтира спорта,
# който ще се практикува от учениците.
# Вход
# От конзолата се четат 4 реда:
# 1.	Сезонът – текст - “Winter”, “Spring” или “Summer”;
# 2.	Видът на групата – текст - “boys”, “girls” или “mixed”;
# 3.	Брой на учениците – цяло число в интервала [1 … 10000];
# 4.	Брой на нощувките – цяло число в интервала [1 … 100].
# Изход
# На конзолата се отпечатва 1 ред:
# •	Спортът, който са практикували учениците и цената за нощувките, която е заплатило училището,
# форматирана до втория знак след десетичната запетая, в следния формат:
# "{спортът} {цената} lv.“
season = input()
group_type = input()
number_of_students = int(input())
number_of_night = int(input())
price_per_night = 0
sport= ""
discount=1
if group_type =="boys" or group_type == "girls":
    if season == "Winter":
        price_per_night = 9.6
    elif season == "Spring":
        price_per_night = 7.2
    else:price_per_night = 15
else:
    if season == "Winter":
        price_per_night = 10
    elif season == "Spring":
        price_per_night = 9.5
    else:price_per_night = 20
if 10 <= number_of_students < 20:
    discount= 0.95
elif 20 <= number_of_students < 50 :
    discount = 0.85
elif number_of_students >= 50 :
    discount = 0.5
if group_type == "girls":
    if season == "Winter":
        sport = "Gymnastics"
    elif season == "Spring":
        sport = "Athletics"
    else:sport = "Volleyball"
elif group_type == "boys":
    if season == "Winter":
        sport = "Judo"
    elif season == "Spring":
        sport = "Tennis"
    else:sport = "Football"
else:
    if season == "Winter":
        sport = "Ski"
    elif season == "Spring":
        sport = "Cycling"
    else:sport = "Swimming"
total_price = number_of_night * number_of_students * price_per_night * discount
print(f"{sport} {total_price:.2f} lv.")