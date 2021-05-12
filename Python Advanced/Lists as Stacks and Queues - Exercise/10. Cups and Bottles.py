from collections import deque

cups = deque([int(el) for el in input().split()])
bottles = [int(el) for el in input().split()]
wasted_water = 0

while len(bottles) > 0 and len(cups) > 0:
    curr_cup = cups[0]
    curr_bottle = bottles.pop()
    if curr_cup > 0:
        if curr_cup <= curr_bottle:
            wasted_water += abs(curr_bottle - curr_cup)
            curr_bottle -= curr_cup
            cups.popleft()
        else:
            while curr_cup > curr_bottle:
                curr_cup -= curr_bottle
                curr_bottle = bottles.pop()

            wasted_water += abs(curr_bottle - curr_cup)
            curr_bottle -= curr_cup
            cups.popleft()

if bottles:
    print(f"Bottles: {' '.join(reversed([str(el) for el in bottles]))}")


else:
    print(f"Cups: {' '.join([str(el) for el in cups])}")
print(f"Wasted litters of water: {wasted_water}")
