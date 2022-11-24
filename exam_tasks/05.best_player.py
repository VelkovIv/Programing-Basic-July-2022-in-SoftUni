command = input()
best_player_name = ""
most_goals_number = 0
while command != "END":
    football_player_name = command
    current_goals_number = int(input())
    if current_goals_number > most_goals_number:
        best_player_name = football_player_name
        most_goals_number = current_goals_number
    if most_goals_number >= 10:
        break
    command = input()
print(f"{best_player_name} is the best player!")
if most_goals_number >= 3:
    print(f"He has scored {most_goals_number} goals and made a hat-trick !!!")
else:
    print(f"He has scored {most_goals_number} goals.")