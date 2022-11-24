# Напишете програма, в която Марин решава задачи от изпити, докато не получи съобщение "Enough" от лектора си.
# При всяка решена задача той получава оценка.
# Програмата трябва да приключи прочитането на данни при команда "Enough" или ако Марин получи
# определения брой незадоволителни оценки. Незадоволителна е всяка оценка, която е по-малка или равна на 4.
# Вход
# •	На първи ред - брой незадоволителни оценки - цяло число;
# •	След това многократно се четат по два реда:
# o	Име на задача – текст;
# o	Оценка - цяло число в интервала [2…6]
# Изход
# •	Ако Марин стигне до командата "Enough", отпечатайте на 3 реда:
# o	"Average score: {средна оценка}"
# o	"Number of problems: {броя на всички задачи}"
# o	"Last problem: {името на последната задача}"
# •	Ако получи определеният брой незадоволителни оценки:
# o	"You need a break, {брой незадоволителни оценки} poor grades."
# Средната оценка да бъде форматирана до втория знак след десетичната запетая.
max_fails = int(input())
task_grade = 0
total_grade = 0
faild_pass = 0
task_counter = 0

while True:
    task_name = input()

    if task_name == 'Enough':
        average = total_grade / task_counter
        print(f"Average score: {average:.2f}")
        print(f"Number of problems: {task_counter}")
        print(f"Last problem: {last_task}")
        break
    task_counter += 1
    task_grade = int(input())
    if task_grade <= 4:
        faild_pass += 1
        if faild_pass == max_fails:
            print(f"You need a break, {faild_pass} poor grades.")
            break
    total_grade += task_grade
    last_task = task_name