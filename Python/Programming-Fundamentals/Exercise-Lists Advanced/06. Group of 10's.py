numbers = [int(num) for num in input().split(",")]
group = 10
while numbers:
    list_num = []
    for number in numbers:
        number = int(number)
        if group - 10 < number <= group:
            list_num.append(number)
    for num1 in list_num:
        if num1 in numbers:
            numbers.remove(num1)
    print(f"Group of {group}'s: {list_num}")

    group += 10
