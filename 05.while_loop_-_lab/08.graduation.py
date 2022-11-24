# Напишете програма, която изчислява средната оценка на ученик от цялото му обучение.
# На първия ред ще получите името на ученика, а на всеки следващ ред неговите годишни оценки.
# Ученикът преминава в следващия клас, ако годишната му оценка е по-голяма или равна на 4.00.
# Ако ученикът бъде скъсан повече от един път, то той бива изключен и програмата приключва,
# като се отпечатва името на ученика и в кой клас бива изключен.
#  При успешно завършване на 12-ти клас да се отпечата :
# "{име на ученика} graduated. Average grade: {средната оценка от цялото обучение}"
# В случай, че ученикът е изключен от училище, да се отпечата:
# "{име на ученика} has been excluded at {класа, в който е бил изключен} grade"
# Стойността трябва да бъде форматирана до втория знак след десетичната запетая.
name = input()

current_year = 0
not_pass =0
total_grade = 0

while True :
    year_grade = float(input())
    current_year +=1

    if year_grade < 4 :
        not_pass +=1
        if not_pass == 2:
            print(f"{name} has been excluded at {current_year} grade")
            break
        # total_grade += year_grade
        current_year -= 1

    else:
        total_grade +=year_grade

    if current_year ==12:
        average = total_grade / 12
        print(f"{name} graduated. Average grade: {average:.2f}")
        break



