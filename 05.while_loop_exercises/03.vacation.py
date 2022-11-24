# Джеси е решила да събира пари за екскурзия и иска от вас да ѝ помогнете да разбере дали ще успее
# да събере необходимата сума. Тя спестява или харчи част от парите си всеки ден.
# Ако иска да похарчи повече от наличните си пари, то тя ще похарчи колкото има и ще ѝ останат 0 лева.
# Вход
# От конзолата се четат:
# •	Пари, нужни за екскурзията - реално число;
# •	Налични пари - реално число.
# След това многократно се четат по два реда:
# •	Вид действие – текст с две възможности: "spend" или "save";
# •	Сумата, която ще спести/похарчи - реално число.
# Изход
# Програмата трябва да приключи при следните случаи:
# •	Ако 5 последователни дни Джеси само харчи, на конзолата да се изпише:
# o	"You can't save the money."
# o	"{Общ брой изминали дни}"
# •	Ако Джеси събере парите за почивката, на конзолата се изписва:
# o	"You saved the money for {общ брой изминали дни} days."
trip_money = float(input())
total_amount = float(input())
days_counter = 0
spend = 0

while True:
    money_movement = input()
    amount = float(input())
    days_counter += 1
    if money_movement == 'save':
        total_amount += amount
        spend = 0
    elif money_movement == 'spend':
        total_amount -= amount
        spend += 1
        if total_amount < 0 :
            total_amount =0
    if spend == 5 :
        print("You can't save the money.")
        print(days_counter)
        break
    if total_amount >= trip_money :
        print(f"You saved the money for {days_counter} days.")
        break