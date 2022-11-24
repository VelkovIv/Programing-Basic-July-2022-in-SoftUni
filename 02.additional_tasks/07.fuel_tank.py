# Напишете програма, която познава дали резервоара на едно превозно средство има нужда от презареждане на горивото или не.
# От конзолата се четат два реда – текст и реално число, на първия ред се чете типа на горивото –
# текст с възможности: "Diesel", "Gasoline" или "Gas", а на втория литрите гориво, които има в резервоара.
# Ако литрите гориво са повече или равни на 25, на конзолата да се отпечата "You have enough {вида на горивото}.",
# ако са по-малко от 25, да се отпечата "Fill your tank with {вида на горивото}!".
# В случай, че бъде въведено гориво, различно от посоченото, да се отпечата "Invalid fuel!".

entered_fiel = input()
fuel_in_tank = int(input())

if entered_fiel == "Diesel":
    refuel = "diesel"
elif entered_fiel == "Gasoline":
    refuel = "gasoline"
elif entered_fiel == "Gas" :
    refuel = "gas"
else: refuel = "Invalid fuel!"

if refuel == "Invalid fuel!":
    print(refuel)
elif fuel_in_tank >= 25:
    print(F"You have enough {refuel}.")
else: print(f"Fill your tank with {refuel}!")