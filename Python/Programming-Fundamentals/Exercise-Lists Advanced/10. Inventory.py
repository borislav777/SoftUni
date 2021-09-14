def is_exist(ite):
    if ite in items:
        return True
    return False


def collect(ite):
    if not is_exist(ite):
        return items.append(ite)


def drop(ite):
    if is_exist(ite):
        return items.remove(ite)


def combine_items(old_ite, new_ite):
    if is_exist(old_ite):
        return items.insert(items.index(old_ite) + 1, new_ite)


def renew(ite):
    if is_exist(ite):
        items.remove(ite)
        items.append(ite)


items = input().split(", ")
command = input()

while not command == "Craft!":
    com, item = command.split(" - ")
    if com == "Collect":
        collect(item)
    elif com == "Drop":
        drop(item)
    elif com == "Combine Items":
        old, new = item.split(":")
        combine_items(old, new)

    elif com == "Renew":
        renew(item)
    command = input()
print(*items, sep=", ")
