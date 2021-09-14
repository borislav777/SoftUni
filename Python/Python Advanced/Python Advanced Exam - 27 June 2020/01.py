from collections import deque

bomb_effects = deque([int(el) for el in input().split(", ")])
bomb_casings = [int(el) for el in input().split(", ")]
datura_bombs = 0
cherry_bombs = 0
smoke_bombs = 0
is_ok = False
while bomb_casings and bomb_effects:
    curr_casing = bomb_casings.pop()
    curr_effect = bomb_effects.popleft()
    combination = curr_casing + curr_effect

    if combination == 40:
        datura_bombs += 1
    elif combination == 60:
        cherry_bombs += 1
    elif combination == 120:
        smoke_bombs += 1
    else:
        curr_casing -= 5
        bomb_casings.append(curr_casing)
        bomb_effects.appendleft(curr_effect)

    if datura_bombs >= 3 and cherry_bombs >= 3 and smoke_bombs >= 3:
        is_ok = True
        break

if is_ok:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(el) for el in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(el) for el in bomb_casings])}")
else:
    print("Bomb Casings: empty")
print(f"Cherry Bombs: {cherry_bombs}")
print(f"Datura Bombs: {datura_bombs}")
print(f"Smoke Decoy Bombs: {smoke_bombs}")
