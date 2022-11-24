movie_budget = float(input())
destination = input()
season = input()
days = int(input())
discount = 1
if destination == "Dubai":
    if season == "Winter":
        price_per_day = 45000
    else:price_per_day = 40000
    discount = 0.7
elif destination == "Sofia":
    if season == "Winter":
        price_per_day = 17000
    else:price_per_day = 12500
    discount = 1.25
elif destination == "London":
    if season == "Winter":
        price_per_day = 24000
    else:price_per_day = 20250

total_movie_price = price_per_day * days * discount
diff = abs(movie_budget - total_movie_price)
if movie_budget >= total_movie_price:
    print(f"The budget for the movie is enough! We have {diff:.2f} leva left!")
else:
    print(f"The director needs {diff:.2f} leva more!")