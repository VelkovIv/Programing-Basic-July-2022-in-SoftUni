tv_show_name = input()
season_number = int(input())
series_number = int(input())
series_lenght = float(input())

real_series_lenght = series_lenght * 1.2
specias_series = season_number * 10
total_tv_show_lenght = real_series_lenght * series_number * season_number + specias_series
print(f"Total time needed to watch the {tv_show_name} series is {total_tv_show_lenght:.0f} minutes.")