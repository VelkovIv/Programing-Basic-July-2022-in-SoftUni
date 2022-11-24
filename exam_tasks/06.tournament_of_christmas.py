tournament_days = int(input())
total_money = 0
winning_days = 0
losing_days = 0

for days in range(tournament_days):
    earned_daily_money = 0
    win_game_counter = 0
    lose_game_counter = 0
    command = input()
    while command != "Finish":
        # game = command
        game_result = input()
        if game_result == "win":
            earned_daily_money +=20
            win_game_counter +=1
        else:
            lose_game_counter +=1
        command = input()
    if win_game_counter > lose_game_counter:
        earned_daily_money *= 1.1
        winning_days +=1
    else:
        losing_days +=1
    total_money += earned_daily_money
if winning_days>losing_days:
    total_money *= 1.2
    print(f"You won the tournament! Total raised money: {total_money:.2f}")
else:
    print(f"You lost the tournament! Total raised money: {total_money:.2f}")