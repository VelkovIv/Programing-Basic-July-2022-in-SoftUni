standard_ticketa = 0
kid_tickets = 0
student_tickets = 0
total_tickets = 0
movie_name = input()
while movie_name != "Finish":
    hall_seats = int(input())
    sold_tickects = 0
    for free_tickets in range(hall_seats):
        type_of_ticket = input()
        if type_of_ticket == "End":
            # is_finish = True
            break
        if type_of_ticket == "student":
            student_tickets += 1
        elif type_of_ticket == "standard":
            standard_ticketa += 1
        elif type_of_ticket == "kid":
            kid_tickets += 1
        sold_tickects += 1


    persentaige_fulful = sold_tickects / hall_seats * 100
    print(f"{movie_name} - {persentaige_fulful:.2f}% full.")
    # total_tickets += total_movie_tickets
    # total_student_tickets += student_ticket
    # total_standard_tickets += standard_ticket
    # total_kid_tickets += kid_ticket
    movie_name = input()
total_tickets = standard_ticketa + student_tickets + kid_tickets
print(f"Total tickets: {total_tickets}")
percent_students_tickects = student_tickets / total_tickets * 100
percent_standard_tickects = standard_ticketa / total_tickets * 100
percent_kid_tickects = kid_tickets / total_tickets * 100
print(f"{percent_students_tickects:.2f}% student tickets.")
print(f"{percent_standard_tickects:.2f}% standard tickets.")
print(f"{percent_kid_tickects:.2f}% kids tickets.")
