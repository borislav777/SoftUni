from collections import deque

quantity_water = int(input())

people = deque()
name = input()
while not name == "Start":
    people.append(name)
    name = input()
command = input()
while not command == "End":
    if command.startswith("refill"):
        split_command = command.split()
        quantity_water += int(split_command[1])
    else:
        if quantity_water >= int(command):
            quantity_water -= int(command)
            print(f"{people.popleft()} got water")
        else:
            print(f"{people.popleft()} must wait")

    command = input()
print(f"{quantity_water} liters left")
