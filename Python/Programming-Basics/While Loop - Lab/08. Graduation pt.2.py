name_student = input()
graduate = float(input())
an_average_grade = 0
next_class = 0
number_of_shutdowns = 0

while number_of_shutdowns <= 2:
    an_average_grade += graduate
    next_class += 1

    if graduate < 4:
        number_of_shutdowns += 1
        print(f"{name_student} has been excluded at {next_class} grade")
        break

    if next_class == 12:
        an_average_grade /= next_class
        print(f"{name_student} graduated. Average grade: {an_average_grade:.2f}")
        break
    graduate = float(input())
