def exist(it):
    if it in groceries:
        return True
    return False


def urgent(it):
    if not exist(it):
        groceries.insert(0, it)


def unnecessary(it):
    if exist(it):
        groceries.remove(it)


def correct(old_ite, new_ite):
    if exist(old_ite):
        groceries[groceries.index(old_ite)] = new_ite


def rearrange(ite):
    if exist(ite):
        groceries.remove(ite)
        groceries.append(ite)


groceries = []
grocer = [groceries.append(el) for el in input().split("!") if el not in groceries]

command = input()

while not command == "Go Shopping!":
    split_comm = command.split()
    if split_comm[0] == "Urgent":
        urgent(split_comm[1])
    elif split_comm[0] == "Unnecessary":
        unnecessary(split_comm[1])
    elif split_comm[0] == "Correct":

        correct(split_comm[1], split_comm[2])
    elif split_comm[0] == "Rearrange":
        rearrange(split_comm[1])
    command = input()

print(', '.join(groceries))


