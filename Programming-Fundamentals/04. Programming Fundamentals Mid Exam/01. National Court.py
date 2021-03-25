first_employee = int(input())
second_employee = int(input())
third_employee = int(input())
people_count = int(input())
people_per_hour = first_employee + second_employee + third_employee
need_hours = 0
while people_count > 0:
    need_hours += 1
    if not need_hours % 4 == 0:
        people_count -= people_per_hour

print(f"Time needed: {need_hours}h.")
