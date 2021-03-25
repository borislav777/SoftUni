jury = int(input())
command = input()
final_grade = 0
count_presentation = 0
while command != "Finish":
    presentation = command
    average_grade = 0
    for exam in range(jury):
        grade = float(input())
        average_grade += grade
        count_presentation += 1
    final_grade += average_grade
    average_grade = average_grade / jury

    print(f"{presentation} - {average_grade:.2f}.")
    command = input()
final_grade = final_grade / count_presentation
print(f"Student's final assessment is {final_grade:.2f}.")
