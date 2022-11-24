# Предстои Вело състезание за благотворителност в което участниците са разпределени в младша("juniors") и
# старша("seniors") група. Парите се набавят от таксата за участие на велосипедистите.
# Според възрастовата група и вида на трасето на което ще се провежда състезанието, таксата е различна.
# Група	    trail	cross-country	downhill	road
# juniors	5.50	8	            12.25	    20
# seniors	7	    9.50	        13.75	    21.50
# Ако в "cross-country" състезанието се съберат 50 или повече участника(общо младши и старши), таксата  намалява с 25%.
# Организаторите отделят 5% процента от събраната сума за разходи.
# Вход
# От конзолата се четат 2 числа и един стринг, всяко на отделен ред:
# •	Първият ред – броят младши велосипедисти. Цяло число в интервала [1…100]
# •	Вторият ред – броят старши велосипедисти. Цяло число в интервала [1… 100]
# •	Третият ред – вид трасе – "trail", "cross-country", "downhill" или "road"
# Изход
# Да се отпечата на конзолата едно число:
# "{дарената сума}" - форматирана с точност до 2 знака след десетичната запетая.
junior_cyclists = int(input())
senior_cyclists = int(input())
track_type = input()
total_income = 0
if track_type == "trail" :
    total_income = junior_cyclists * 5.5 +  senior_cyclists * 7
elif track_type == "cross-country" :
    total_income = junior_cyclists * 8 + senior_cyclists * 9.5
    if junior_cyclists + senior_cyclists >= 50:
        total_income = total_income * 0.75
elif track_type == "downhill" :
    total_income = junior_cyclists * 12.25 + senior_cyclists * 13.75
else:
    total_income = junior_cyclists * 20 + senior_cyclists * 21.5
finale_income = total_income * 0.95
print(f"{finale_income:.2f}")