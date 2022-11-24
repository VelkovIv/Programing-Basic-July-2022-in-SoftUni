from math import floor

time_first_runner = int(input())
time_second_runner = int(input())
time_third_runner = int(input())
total_time= time_first_runner + time_second_runner + time_third_runner
minutes = floor(total_time // 60)
seconds = total_time - (minutes * 60)
if seconds <10 :
    print(f"{minutes}:0{seconds}")
else: print(f"{minutes}:{seconds}")
