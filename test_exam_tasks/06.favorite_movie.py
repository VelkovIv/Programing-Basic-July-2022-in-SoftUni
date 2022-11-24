movie_name = input()
movie_counter = 0

bigger_score =0
best_movie = ""
while movie_name != "STOP":
    movie_counter += 1
    name_lenght = len(movie_name)
    score = 0
    for index,digit in enumerate(movie_name):
        if 97 <= ord(digit) <= 122:
            score += ord(digit) - 2 * name_lenght
        elif 65 <= ord(digit) <= 90:
            score += ord(digit) - name_lenght
        else:
            score += ord(digit)
    if score > bigger_score:
        bigger_score = score
        best_movie = movie_name
    if movie_counter == 7:
        break
    movie_name = input()
if movie_counter == 7:
    print("The limit is reached.")
print(f"The best movie for you is {best_movie} with {bigger_score} ASCII sum.")