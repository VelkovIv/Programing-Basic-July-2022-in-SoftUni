# Производителите на вендинг машини искали да направят машините си да връщат възможно най-малко монети ресто.
# Напишете програма, която приема сума - рестото,
# което трябва да се върне и изчислява с колко най-малко монети може да стане това.
change = float(input())
coints_counter = 0

while change != 0:
    change = round(change, 2)
    if change >= 2:
        change -= 2
        coints_counter += 1
    elif change >= 1:
        change -= 1
        coints_counter += 1
    elif change >= 0.50:
        change -= 0.5
        coints_counter += 1
    elif change >= 0.4 :
        change -= 0.4
        coints_counter += 2
    elif change >= 0.2 :
        change -= 0.2
        coints_counter += 1
    elif change >= 0.1 :
        change -= 0.1
        coints_counter += 1
    elif change >= 0.05 :
        change -= 0.05
        coints_counter += 1
    elif change >= 0.04 :
        change -= 0.04
        coints_counter += 2
    elif change >= 0.02 :
        change -= 0.02
        coints_counter += 1
    elif change >= 0.01 :
        change -= 0.01
        coints_counter += 1

print(coints_counter)