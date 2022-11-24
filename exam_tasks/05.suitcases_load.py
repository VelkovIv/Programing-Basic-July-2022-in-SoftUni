airplane_trunk_volume = float(input())
suitcase_counter = 0
trunk_is_full = False
command = input()
while command != "End":
    suitcase_volume = float(command)
    if airplane_trunk_volume < suitcase_volume:
        print("No more space!")
        break
    suitcase_counter += 1
    if suitcase_counter % 3 == 0:
        suitcase_volume *= 1.1
    airplane_trunk_volume -= suitcase_volume
    command = input()
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcase_counter} suitcases loaded.")
