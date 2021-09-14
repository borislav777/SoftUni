n = int(input())
first_number = 0
second_number = 0
for number in range(0, n):
    value = int(input())
    first_number += value
for number in range(0, n):
    value = int(input())
    second_number += value

if first_number == second_number:
    print(f"Yes, sum = {first_number}")
else:
    print(f"No, diff = {abs(first_number - second_number)}")
