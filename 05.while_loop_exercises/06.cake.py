# Поканени сте на 30-ти рожден ден, на който рожденикът черпи с огромна торта.
# Той обаче не знае колко парчета могат да си вземат гостите от нея.
# Вашата задача е да напишете програма, която изчислява броя на парчетата, които гостите са взели преди тя да свърши.
# Ще получите размерите на тортата (широчина и дължина – цели числа и след това на всеки ред,
# до получаване на командата "STOP" или докато не свърши тортата, броят на парчетата, които гостите вземат от нея.
# Всяко парче торта е с размер 1х1 см.
# Да се отпечата на конзолата един от следните редове:
# •	"{брой парчета} pieces are left." - ако стигнете до STOP и не са свършили парчетата торта;
# •	"No more cake left! You need {брой недостигащи парчета} pieces more."
cake_lenght = int(input())
cake_width = int(input())
cake_pcs = cake_width * cake_lenght

while cake_pcs != 0:
    needed_cake_pcs = input()
    if needed_cake_pcs == 'STOP':
        print(f"{cake_pcs} pieces are left.")
        break
    needed_cake_pcs = int(needed_cake_pcs)
    cake_pcs -= needed_cake_pcs
    if cake_pcs < 0 :
        print(f"No more cake left! You need {abs(cake_pcs)} pieces more.")
        break