# Григор Димитров е тенисист, чиято следваща цел е изкачването в световната ранглиста по тенис за мъже.
# През годината Гришо участва в определен брой турнири, като за всеки турнир получава точки,
# които зависят от позицията, на която е завършил в турнира. Има три варианта за завършване на турнир:
# 	W - ако е победител получава 2000 точки
# 	F - ако е финалист получава 1200 точки
# 	SF - ако е полуфиналист получава 720 точки
# Напишете програма, която изчислява колко ще са точките на Григор след изиграване на всички турнири,
# като знаете с колко точки стартира сезона. Също изчислете колко точки средно печели от всички изиграни турнири
# и колко процента от турнирите е спечелил.
# Вход
# От конзолата първо се четат два реда:
# •	Брой турнири, в които е участвал – цяло число в интервала [1…20]
# •	Начален брой точки в ранглистата - цяло число в интервала [1...4000]
# За всеки турнир се прочита отделен ред:
# •	Достигнат етап от турнира – текст – "W", "F" или "SF"
# Изход
# Отпечатват се три реда в следния формат:
# •	"Final points: {брой точки след изиграните турнири}"
# •	"Average points: {средно колко точки печели за турнир}"
# •	"{процент спечелени турнири}%"
# Средните точки да бъдат закръглени към най-близкото цяло число надолу, а процентът да се форматира до втората цифра след десетичния знак.
from math import floor

tournament_numbers = int(input())
preliminaly_points = int(input())

w=0
tournament_points = 0
for _ in range(tournament_numbers):
    stage = input()
    if stage == "W":
        tournament_points += 2000
        w +=1
    elif stage == "F" :
        tournament_points += 1200
    else:
        tournament_points += 720
average_points = floor(tournament_points / tournament_numbers)
tournament_won = w/tournament_numbers

print(f"Final points: {tournament_points+preliminaly_points}")
print(f"Average points: {average_points}")
print(f"{tournament_won*100:.2f}%")