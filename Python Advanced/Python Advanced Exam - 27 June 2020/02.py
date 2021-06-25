def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


lair_size = int(input())

lair = []
position = None
burrows = []
directions = {'right': (0, +1), 'left': (0, -1), 'up': (-1, 0), 'down': (+1, 0)}
food = 0
game_over = False
for row in range(lair_size):
    new_row = list(input())
    lair.append(new_row)
    if "S" in new_row:
        position = row, new_row.index("S")
    elif 'B' in new_row:
        burrows.append((row, new_row.index("B")))

while food < 10:
    direction = input()
    r, c = position
    row, col = r + directions[direction][0], c + directions[direction][1]
    if is_valid(row, col, lair_size):
        if lair[row][col] == "*":
            food += 1
            position = row, col
        elif lair[row][col] == 'B':
            burrows.remove((row, col))
            lair[r][c] = '.'
            lair[row][col] = '.'
            position = burrows[0]
            burrows.pop()
            continue

        lair[r][c] = '.'
        lair[row][col] = 'S'
        position = row,col
    else:
        lair[r][c] = '.'
        game_over = True
        break

if game_over:
    print("Game over!")
else:
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
[print(*r,sep="") for r in lair]
