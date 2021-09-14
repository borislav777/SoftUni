number_line = int(input())
numbers = []
filtered = []
for num in range(number_line):
    number = int(input())
    numbers.append(number)
command = input()
for num_1 in numbers:
    if command == "even":
        if num_1 % 2 == 0:
            filtered.append(num_1)
    elif command == "odd":
        if not num_1 % 2 == 0:
            filtered.append(num_1)
    elif command == "negative":
        if num_1 < 0:
            filtered.append(num_1)
    elif command == "positive":
        if num_1 >= 0:
            filtered.append(num_1)
print(filtered)
