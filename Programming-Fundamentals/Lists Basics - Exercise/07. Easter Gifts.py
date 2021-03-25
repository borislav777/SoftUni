names_gift = input().split()
command = input()
while not command == "No Money":
    case = command.split()
    if "OutOfStock" in case:
        for gift in range(len(names_gift)):
            if case[1] == names_gift[gift]:
                names_gift[gift] = "None"
    elif "Required" in case:
        index_case = int(case[2])
        if 0 < index_case < len(names_gift):
            names_gift[index_case] = case[1]
    elif "JustInCase" in case:
        names_gift[len(names_gift) - 1] = case[1]
    command = input()
while "None" in names_gift:
    names_gift.remove("None")


print(" ".join(names_gift))
