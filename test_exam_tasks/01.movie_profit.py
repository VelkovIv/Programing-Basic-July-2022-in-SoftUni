movie_name = input()
days = int(input())
ticket_numbers = int(input())
ticket_price = float(input())
percent_for_cinema = int(input())

total_ticket_income = ticket_price * ticket_numbers * days
final_ticket_income = total_ticket_income - (total_ticket_income * percent_for_cinema /100)
print(f"The profit from the movie {movie_name} is {final_ticket_income:.2f} lv.")
