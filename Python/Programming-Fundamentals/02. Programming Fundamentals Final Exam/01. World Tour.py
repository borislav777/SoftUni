def is_valid(index):
    if index in range(len(destinations)):
        return True
    return False


destinations = input()
command = input()

while not command == "Travel":
    manipulations = command.split(":")
    manipulation = manipulations[0]
    if manipulation == "Add Stop":
        index = int(manipulations[1])
        string = manipulations[2]
        if is_valid(index):
            destinations = destinations[:index] + string + destinations[index:]
        print(destinations)

    elif manipulation == "Remove Stop":
        start_index = int(manipulations[1])
        end_index = int(manipulations[2])
        if is_valid(start_index) and is_valid(end_index):
            cut = destinations[start_index:end_index + 1]
            destinations = destinations.replace(cut, "", 1)
        print(destinations)

    elif manipulation == "Switch":
        old_string = manipulations[1]
        new_string = manipulations[2]
        if old_string in destinations:
            destinations = destinations.replace(old_string, new_string)
        print(destinations)

    command = input()

print(f"Ready for world tour! Planned stops: {destinations}")
