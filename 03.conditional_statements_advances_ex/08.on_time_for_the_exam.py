# Студент трябва да отиде на изпит в определен час (например в 9:30 часа).
# Той идва в изпитната зала в даден час на пристигане (например 9:40).
# Счита се, че студентът е дошъл навреме, ако е пристигнал в часа на изпита или до половин час преди това.
# Ако е пристигнал по-рано повече от 30 минути, той е подранил. Ако е дошъл след часа на изпита, той е закъснял.
# Напишете програма, която прочита време на изпит и време на пристигане и отпечатва дали студентът е дошъл навреме,
# дали е подранил или е закъснял и с колко часа или минути е подранил или закъснял.
# Вход
# От конзолата се четат 4 цели числа (по едно на ред), въведени от потребителя:
# •	Първият ред съдържа час на изпита - цяло число от 0 до 23;
# •	Вторият ред съдържа минута на изпита - цяло число от 0 до 59;
# •	Третият ред съдържа час на пристигане - цяло число от 0 до 23;
# •	Четвъртият ред съдържа минута на пристигане - цяло число от 0 до 59.
# Изход
# На първия ред отпечатайте:
# •	"Late", ако студентът пристига по-късно от часа на изпита;
# •	"On time", ако студентът пристига точно в часа на изпита или до 30 минути по-рано;
# •	"Early", ако студентът пристига повече от 30 минути преди часа на изпита.
# Ако студентът пристига с поне минута разлика от часа на изпита, отпечатайте на следващия ред:
# •	"mm minutes before the start" за идване по-рано с по-малко от час;
# •	"hh:mm hours before the start" за подраняване с 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:05”;
# •	 "mm minutes after the start" за закъснение под час;
# •	"hh:mm hours after the start" за закъснение от 1 час или повече. Минутите винаги печатайте с 2 цифри, например "1:03”.
exam_hour = int(input())
exam_minutes = int(input())
arrival_hour = int(input())
arrival_minutes = int(input())

exam_time = exam_hour * 60 + exam_minutes
arrival_time = arrival_hour * 60 +arrival_minutes
diff = abs(exam_time - arrival_time)
hour = diff // 60
minutes = diff % 60

if exam_time < arrival_time :
    print("Late")
    if diff < 60:
            print(f"{minutes} minutes after the start")
    else:   print(f"{hour}:{minutes:02d} hours after the start")

elif exam_time >= arrival_time and diff<=30:
    print("On time")
    if diff >= 1:
        print(f"{minutes} minutes before the start")
else:
    print("Early")
    if diff < 60:
        print(f"{minutes} minutes before the start")
    else:
        print(f"{hour}:{minutes:02d} hours before the start")


# exam_hour = int(input())
# exam_min = int(input())
# arrival_hour = int(input())
# arrival_min = int(input())
#
# exam_time_min = (exam_hour * 60) + exam_min
# arrival_time_min = (arrival_hour * 60) + arrival_min
#
# diff_min = abs(exam_time_min - arrival_time_min)
# if exam_time_min < arrival_time_min:
#     print("Late")
#     if diff_min >= 60:
#         hour = diff_min // 60
#         minutes = diff_min % 60
#         print(f"{hour}:{minutes:02d} hours after the start")
#     else:
#         print(f"{diff_min} minutes after the start")
# elif exam_time_min == arrival_time_min or diff_min <= 30:
#     print("On time")
#     if diff_min >= 1:
#         print(f"{diff_min} minutes before the start")
# else:
#     print("Early")
#     if diff_min >= 60:
#         hour = diff_min // 60
#         minutes = diff_min % 60
#         print(f"{hour}:{minutes:02d} hours before the start")
#     else:
#         print(f"{diff_min} minutes before the start")