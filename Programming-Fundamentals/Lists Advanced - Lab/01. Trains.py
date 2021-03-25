number_wagons = int(input())
wagons = [0] * number_wagons
command = input()

while not command == "End":
    split_command = command.split()
    if split_command[0] == "add":
        people = int(split_command[1])
        wagons[-1] += people
    elif split_command[0] == "insert":
        index = int(split_command[1])
        people = int(split_command[2])
        wagons[index] += people
    elif split_command[0] == "leave":
        index = int(split_command[1])
        people = int(split_command[2])
        wagons[index] -= people
    command = input()
print(wagons)