import sys

command = input()
min_sum = sys.maxsize

while command != "Stop":
    number = int(command)
    if min_sum > number:
        min_sum = number
    command = input()
print(min_sum)
