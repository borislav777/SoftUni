elements = input().split()
command = input()
moves = 0
is_lose = True
while not command == "end":
    index1, index2 = command.split()
    index1 = int(index1)
    index2 = int(index2)
    moves += 1
    if index1 == index2 or not index1 in range(len(elements)) or not index2 in range(len(elements)):
        elements.insert(int(len(elements) / 2), f"-{moves}a")
        elements.insert(int(len(elements) / 2), f"-{moves}a")
        print("Invalid input! Adding additional elements to the board")

    elif elements[index1] == elements[index2]:
        print(f"Congrats! You have found matching elements - {elements[index1]}!")
        current_element = elements[index1]
        elements.pop(index1)
        elements.remove(current_element)
    else:
        print("Try again!")
    if len(elements) == 0:
        print(f"You have won in {moves} turns!")
        is_lose = False
        break

    command = input()

if is_lose:
    print("Sorry you lose :(")
    print(*elements)
