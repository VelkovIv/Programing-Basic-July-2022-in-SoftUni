# Напишете програма, която да умножава положителни числа по 2.
# От конзолата се четат поредица от реални числа, всяко на нов ред, докато не се въведе отрицателно.
# След всяко умножено число на нов ред да се отпечата "Result: {резултата от умножението}".
# Резултата от умножението да бъде форматиран до втория знак след десетичния разделител.
# При получаване на негативно число, на конзолата да се отпечата "Negative number!" и програмата да приключи изпълнение.
x=1
while x >= 0 :
    x = float(input())
    if x >= 0 :
        x = x * 2
        print(f"Result: {x:.2f}")
    else:
        print("Negative number!")
        break