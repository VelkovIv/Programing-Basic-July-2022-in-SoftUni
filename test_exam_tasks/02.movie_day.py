schooting_time = int(input())
scene_numbers = int(input())
scene_time = int(input())

preparation_time = schooting_time * 0.15
total_time = scene_time * scene_numbers + preparation_time
diff=abs(schooting_time - total_time)
if schooting_time >= total_time:
    print(f"You managed to finish the movie on time! You have {diff:.0f} minutes left!")
else:
    print(f"Time is up! To complete the movie you need {diff:.0f} minutes.")