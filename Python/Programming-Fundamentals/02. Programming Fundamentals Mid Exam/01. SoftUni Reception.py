first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
total_help = first_employee + second_employee + third_employee
student_count = int(input())
hours = 0

while student_count > 0:
    hours += 1
    if hours % 4 == 0:
        continue
    student_count -= total_help

print(f"Time needed: {hours}h.")
