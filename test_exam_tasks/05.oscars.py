acthor_name = input()
academy_points = float(input())
judge_nimbers = int(input())

judge_points = 0
evaloation_points = academy_points
for _ in range(judge_nimbers) :
    judge_name = input()
    judge_points = float(input())
    evaloation_points += len(judge_name) * judge_points /2
    if evaloation_points >= 1250.5:
        break
if evaloation_points >= 1250.5:
    print(f"Congratulations, {acthor_name} got a nominee for leading role with {evaloation_points:.1f}!")
else:
    print(f"Sorry, {acthor_name} you need {1250.5-evaloation_points:.1f} more!")