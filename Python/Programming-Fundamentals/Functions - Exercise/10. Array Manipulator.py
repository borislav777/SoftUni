def exchange(num, index):
    first_half = num[index + 1:]
    second_half = num[:index + 1]
    return first_half + second_half


def max_num(num):
    if not num:
        return "No matches"
    else:
        return len(data) - data[::-1].index(max(num)) - 1


def min_num(num):
    if not num:
        return "No matches"
    else:
        return len(data) - data[::-1].index(min(num)) - 1


def first(num, count):
    if not num:
        return num
    else:
        return num[:count]


def last(num, count):
    if not num:
        return num
    else:
        num = num[::-1]
        last_num = num[:count]

        return list(reversed(last_num))


data = [int(num) for num in input().split()]
command = input()

while not command == "end":
    split_command = command.split()

    if split_command[0] == "exchange":
        sli = int(split_command[1])
        if 0 <= sli < len(data):
            data = exchange(data, sli)

        else:
            print("Invalid index")


    elif split_command[0] == "max":

        if split_command[1] == "odd":
            odd = [el for el in data if not el % 2 == 0]
            print(max_num(odd))
        elif split_command[1] == "even":
            even = [el for el in data if el % 2 == 0]
            print(max_num(even))

    elif split_command[0] == "min":
        if split_command[1] == "odd":
            odd = [el for el in data if not el % 2 == 0]
            print(min_num(odd))
        elif split_command[1] == "even":
            even = [el for el in data if el % 2 == 0]
            print(min_num(even))

    elif split_command[0] == "first":
        sli = int(split_command[1])
        if sli > len(data):
            print("Invalid count")
        else:
            if split_command[2] == "odd":
                odd = [el for el in data if not el % 2 == 0]
                print(first(odd, sli))
            elif split_command[2] == "even":
                even = [el for el in data if el % 2 == 0]
                print(first(even, sli))

    elif split_command[0] == "last":
        sli = int(split_command[1])
        if sli > len(data):
            print("Invalid count")
        else:
            if split_command[2] == "odd":
                odd = [el for el in data if not el % 2 == 0]
                print(last(odd, sli))
            elif split_command[2] == "even":
                even = [el for el in data if el % 2 == 0]
                print(last(even, sli))
    command = input()
print(data)
