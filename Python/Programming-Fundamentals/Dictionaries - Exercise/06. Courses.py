command = input()
courses = {}
while not command == "end":
    course, student = command.split(" : ")
    if course not in courses:
        courses[course] = [student]
    else:
        courses[course] += [student]
    command = input()

for course, students in sorted(courses.items(), key=lambda x: (-len(x[1]))):

    print(f"{course}: {len(students)}")
    for student in sorted(students, key=lambda x: x):
        print(f"-- {student}")
