import sys

numbers = int(input())
sum = 0
max_number = -sys.maxsize
for number in range(0, numbers):
    value = int(input())
    sum += value
    if value > max_number:
        max_number = value

sum = sum - max_number
if max_number == sum:
    print(f"Yes")
    print(f"Sum = {max_number} ")
else:
    print(f"No")
    print(f"Diff = {abs(max_number - sum)} ")
