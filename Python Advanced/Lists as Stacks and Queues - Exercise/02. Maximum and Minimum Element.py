number_queries = int(input())
numbers = []
for _ in range(number_queries):
    type_command = input()
    if type_command.startswith("1"):
        curr_type, number = type_command.split()
        number = int(number)
        numbers.append(number)
    elif type_command.startswith("2"):
        if numbers:
            numbers.pop()
    elif type_command.startswith("3"):
        if numbers:
            print(max(numbers))

    elif type_command.startswith("4"):
        if numbers:
            print(min(numbers))
numbers.reverse()
print(", ".join([str(el) for el in numbers]))
