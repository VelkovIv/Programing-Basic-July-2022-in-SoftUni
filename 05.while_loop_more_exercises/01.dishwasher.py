# Гошо работи в ресторант и отговаря за зареждането на съдомиялната накрая на деня.
# Вашата задача е да напишете програма, която изчислява, дали дадено закупено количество бутилки от препарат
# за съдомиялна е достатъчно, за да измие определено количество съдове.
# Знае се, че всяка бутилка съдържа 750 мл. препарат, за 1 чиния са нужни 5 мл., а за тенджера 15 мл.
# Приемете, че на всяко трето зареждане със съдове, съдомиялната се пълни само с тенджери, а останалите пъти с чинии.
# Докато не получите команда "End" ще продължите да получавате бройка съдове, които трябва да бъдат измити.
# Вход
# От конзолата се четат:
# •	Брой бутилки от препарат, който ще бъде използван за миенето на чинии - цяло число в интервала [1…10]
# На всеки следващ ред, до получаване на командата "End" или докато количеството препарат не се изчерпи,
# брой съдове, които трябва да бъдат измити - цяло число в интервала [1…100]
# Изход
# В случай, че количеството препарат е било достатъчно за измиването на съдовете:
# "Detergent was enough!"
# "{брой чисти чинии} dishes and {брой чисти тенджери} pots were washed."
# "Leftover detergent {количество останал препарат} ml."
# В случай, че количеството препарат не е било достатъчно за измиването на съдовете:
# "Not enough detergent, {количество не достигнал препарат} ml. more necessary!"
detergent_bottles = int(input())
detergent_ml = detergent_bottles * 750
dishwasher_counter = 0
plates = 0
pots = 0

while True:
    dishes = input()
    if dishes == 'End':
        print("Detergent was enough!")
        print(f"{plates} dishes and {pots} pots were washed.")
        print(f"Leftover detergent {detergent_ml} ml.")
        break
    dishes = int(dishes)
    dishwasher_counter += 1
    if dishwasher_counter % 3 == 0 :
        detergent_ml -= dishes * 15
        pots += dishes
    else:
        detergent_ml -= dishes * 5
        plates += dishes
    if detergent_ml < 0:
        print(f"Not enough detergent, {abs(detergent_ml)} ml. more necessary!")
        break