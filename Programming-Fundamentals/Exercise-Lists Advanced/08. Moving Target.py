def shoot(i, power):
    if 0 <= i < len(targets):

        if targets[i] <= power:
            return targets.pop(i)
        else:
            targets[i] -= power
            return targets[i]


def add(i, val):
    if 0 <= i <= len(targets) - 1:
        return targets.insert(i, val)
    print("Invalid placement!")


def strike(i, radius):
    del targets[i - radius:i + radius + 1]
    return targets


targets = [int(num) for num in input().split()]
command = input()

while not command == "End":
    manipulation, index, value = command.split()
    index = int(index)
    value = int(value)
    if manipulation == "Shoot":
        shoot(index, value)
    elif manipulation == "Add":
        add(index, value)
    elif manipulation == "Strike":
        if 0 <= index <= len(targets):
            if index - value in range(len(targets)) and index + value in range(len(targets)):
                targets = strike(index, value)

            else:
                print("Strike missed!")

    command = input()
targets_as_string = [str(num) for num in targets]
print("|".join(targets_as_string))
