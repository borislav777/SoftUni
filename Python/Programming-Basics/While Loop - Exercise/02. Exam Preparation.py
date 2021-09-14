
number_of_unsatisfactory_assessments = int(input())
command = input()

average_grade = 0
total_exam = 0
count_of_unsatisfactory_assessments = 0
isOff = False
last_exam=""

while command != "Enough":
    last_exam=command
    grade = int(input())
    total_exam += 1
    average_grade += grade
    if grade <= 4:
        count_of_unsatisfactory_assessments += 1
    if count_of_unsatisfactory_assessments == number_of_unsatisfactory_assessments:
        isOff = True
        break
    command = input()

total_average_grade = average_grade / total_exam
if isOff:
    print(f"You need a break, {count_of_unsatisfactory_assessments} poor grades.")
else:
    print(f"Average score: {total_average_grade:.2f}")
    print(f"Number of problems: {total_exam}")
    print(f"Last problem: {last_exam}")
