from collections import deque

chocolate = [int(el) for el in input().split(", ")]
cup_of_milks = deque([int(el) for el in input().split(", ")])
milkshake = 0
is_great = False

while len(chocolate) > 0 and len(cup_of_milks) > 0:

    if chocolate[-1] <= 0:
        chocolate.pop()

    if cup_of_milks[0] <= 0:
        cup_of_milks.popleft()
        continue

    curr_chocolate = chocolate.pop()
    curr_cup = cup_of_milks.popleft()

    if curr_chocolate == curr_cup:
        milkshake += 1
    else:
        cup_of_milks.append(curr_cup)
        curr_chocolate -= 5
        chocolate.append(curr_chocolate)
    if milkshake >= 5:
        is_great = True
        break

if is_great:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolate:
    print(f"Chocolate: {', '.join([str(el) for el in chocolate])}")
else:
    print("Chocolate: empty")
if cup_of_milks:
    print(f"Milk: {', '.join([str(el) for el in cup_of_milks])}")
else:
    print("Milk: empty")
