movie_budget = float(input())
command = input()
no_money = False

while command != "ACTION":
    actior_name = command
    if len(actior_name) > 15:
        movie_budget -= movie_budget * 0.2
    else:
        payment = float(input())
        movie_budget -= payment
    if movie_budget < 0:
        no_money = True
        break
    command = input()
if no_money:
    movie_budget = abs(movie_budget)
    print(f"We need {movie_budget:.2f} leva for our actors.")
else:
    print(f"We are left with {movie_budget:.2f} leva.")