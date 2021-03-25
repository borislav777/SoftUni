def is_exist(ind):
    if len(sequence) > ind >= 0:
        return True
    return False


def shoot(ind, num):
    if is_exist(ind):

        if sequence[ind] <= num:
            return sequence.pop(ind)
        else:
            sequence[ind] -= num
        return sequence[ind]


def add(ind, num):
    if is_exist(ind):
        return sequence.insert(ind, num)
    print("Invalid placement!")


def strike(ind, radius):
    del sequence[ind - radius:ind + radius + 1]


sequence = [int(num) for num in input().split()]
command = input()

while not command == "End":
    comm, index, value = command.split()
    index = int(index)
    value = int(value)

    if comm == "Shoot":
        shoot(index, value)
    elif comm == "Add":
        add(index, value)
    elif comm == "Strike":
        if (index + value) in range(len(sequence)) and (index - value) in range(len(sequence)):
            strike(index, value)
        else:
            print("Strike missed!")
    command = input()

print("|".join([str(el) for el in sequence]))
