initial_treasure = input().split("|")
command = input()

while not command == "Yohoho!":
    split_comm = command.split()
    if split_comm[0] == "Loot":
        for item in split_comm[1:]:
            if item not in initial_treasure:
                initial_treasure.insert(0, item)
    elif split_comm[0] == "Drop":
        index = int(split_comm[1])
        if index in range(len(initial_treasure)):
            element = initial_treasure[index]
            initial_treasure.pop(index)
            initial_treasure.append(element)
    elif split_comm[0] == "Steal":
        count = int(split_comm[1])
        steal = initial_treasure[-count:]
        del initial_treasure[-count:]

        print(", ".join(steal))
    command = input()

length = [int(len(el)) for el in initial_treasure]
sum_el = sum(length)

if len(initial_treasure) == 0:
    print("Failed treasure hunt.")
else:
    avg = sum_el / len(initial_treasure)
    print(f"Average treasure gain: {avg:.2f} pirate credits.")
