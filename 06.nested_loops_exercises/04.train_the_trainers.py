numbers_of_jury = int(input())
presentation_name = input()
presentation_number = 0
final_presentation_grade =0
while presentation_name != "Finish":
    presentation_number += 1
    average_grade = 0
    total_presentation_grade = 0
    for grade in range(numbers_of_jury):
        current_grade = float(input())
        total_presentation_grade += current_grade
    average_grade = total_presentation_grade / numbers_of_jury
    print(f"{presentation_name} - {average_grade:.2f}.")
    final_presentation_grade += average_grade
    presentation_name = input()
average = final_presentation_grade / presentation_number
print(f"Student's final assessment is {average:.2f}.")