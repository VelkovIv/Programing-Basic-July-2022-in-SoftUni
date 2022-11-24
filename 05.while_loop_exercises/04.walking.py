# Габи иска да започне здравословен начин на живот и си е поставила за цел да върви 10 000 стъпки всеки ден.
# Някои дни обаче е много уморена от работа и ще иска да се прибере преди да постигне целта си.
# Напишете програма, която чете от конзолата по колко стъпки изминава тя всеки път като излиза през деня
# и когато постигне целта си да се изписва
# "Goal reached! Good job!" и колко стъпки повече е извървяла "{разликата между стъпките} steps over the goal!"
# Ако иска да се прибере преди това, тя ще въведе командата "Going home" и ще въведе стъпките,
# които е извървяла докато се прибира. След което, ако не е успяла да постигне целта си,
# на конзолата трябва да се изпише: "{разликата между стъпките} more steps to reach goal."
steps_target = 10000
total_steps = 0

while total_steps <= steps_target:
    steps = input()
    if steps == 'Going home':
        steps = input()
        steps = int(steps)
        total_steps += steps
        if total_steps >= steps_target:
            print(f"Goal reached! Good job!")
            print(f"{total_steps - steps_target} steps over the goal!")
        else:
            print(f"{steps_target - total_steps} more steps to reach goal.")
        break
    steps = int(steps)
    total_steps += steps
    if total_steps >= steps_target:
        print(f"Goal reached! Good job!")
        print(f"{total_steps-steps_target} steps over the goal!")