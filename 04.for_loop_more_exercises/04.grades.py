# Напишете програма, която да пресмята статистика на оценки от изпит. В началото програмата получава броят на студентите явили се на изпита и за всеки студент неговата оценка. На края програмата трябва да изпечата процента на студенти с оценка между 2.00 и 2.99, между 3.00 и 3.99, между 4.00 и 4.99, 5.00 или повече. Също така и средният успех на изпита.
# Вход
# От конзолата се четат поредица от числа, всяко на отделен ред:
# •	На първия ред – броя на студентите явили се на изпит – цяло число в интервала [1...1000]
# •	За всеки един студент на отделен ред – оценката от изпита – реално число в интервала [2.00...6.00]
# Изход
# Да се отпечатат на конзолата 5 реда, които съдържат следната информация:
# Ред 1 -	"Top students: {процент студенти с успех 5.00 или повече}%"
# Ред 2 -	"Between 4.00 and 4.99: {между 4.00 и 4.99 включително}%"
# Ред 3 -	"Between 3.00 and 3.99: {между 3.00 и 3.99 включително}%"
# Ред 4 -	"Fail: {по-малко от 3.00}%"
# Ред 5 -	"Average: {среден успех}"
# Всички числа трябва да са форматирани до вторият знак след десетичната запетая.

number_of_students = int(input())

top_students = 0
mid_students =0
low_students = 0
fail_students = 0
total_grades = 0
for i in range(number_of_students):
    exam_grade = float(input())
    if exam_grade >=5 :
        top_students +=1
    elif 4 <= exam_grade < 5 :
        mid_students += 1
    elif 3 <= exam_grade < 4 :
        low_students += 1
    else:
        fail_students +=1
    total_grades += exam_grade

print(f"Top students: {top_students/number_of_students*100:.2f}%")
print(f"Between 4.00 and 4.99: {mid_students/number_of_students*100:.2f}%")
print(f"Between 3.00 and 3.99: {low_students/number_of_students*100:.2f}%")
print(f"Fail: {fail_students/number_of_students*100:.2f}%")
print(f"Average: {total_grades/number_of_students:.2f}")