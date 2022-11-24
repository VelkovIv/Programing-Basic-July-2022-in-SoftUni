# Напишете програма, която чете две цели числа (N1 и N2) и оператор,
# с който да се извърши дадена математическа операция.
# Възможните операции са: Събиране(+), Изваждане(-), Умножение(*),  Деление(/) и Модулно деление(%).
# При събиране, изваждане и умножение на конзолата трябва да се отпечатат резултата и дали той е четен или нечетен
# При обикновеното деление - резултата.
# При модулното деление - остатъка.
# Трябва да се има предвид, че делителят може да е равен на 0 (нула), а на нула не се дели.
# В този случай трябва да се отпечата специално съобщениe.
# Вход
# От конзолата се прочитат 3 реда, въведени от потребителя:
# •	N1 - цяло число;
# •	N2 - цяло число;
# •	Оператор - един символ измежду: "+", "-", "*", "/", "%".
# Изход
# Да се отпечата на конзолата един ред:
# •	Ако операцията е събиране, изваждане или умножение:
# o	 "{N1} {оператор} {N2} = {резултат} - {even/odd}"
# •	Ако операцията е деление:
# o	"{N1} / {N2} = {резултат}" - резултат, форматиран до втория знак след десетичната запетая
# •	Ако операцията е модулно деление:
# o	"{N1} % {N2} = {остатък}"
# •	В случай на деление с 0 (нула):
# o	"Cannot divide {N1} by zero"
number1 = int(input())
number2 = int(input())
operation = input()
result=0
result_type = ""
if number2 == 0 and (operation == "/"or operation == "%"):
    print(f"Cannot divide {number1} by zero")
else:
    if operation == "+":
        result = number1 + number2
        if  result % 2 ==0:
            result_type = "even"
        else: result_type = "odd"
    elif operation == "-":
        result = number1 - number2
        if result % 2 == 0:
            result_type = "even"
        else:
            result_type = "odd"
    elif operation == "*":
        result = number1 * number2
        if result % 2 == 0:
            result_type = "even"
        else:
            result_type = "odd"
    elif operation == "/":
        result = number1 / number2

    elif operation == "%":
        result = number1 % number2
    if result_type == "":
        if operation == "/":
            print(f"{number1} / {number2} = {result:.2f}")
        else: print(f"{number1} % {number2} = {result}")
    else:
        print(f"{number1} {operation} {number2} = {result} - {result_type}")
