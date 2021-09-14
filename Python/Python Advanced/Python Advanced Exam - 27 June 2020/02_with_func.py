def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


def fill_lair(n):
    lair = []
    burrows = []
    position = None
    for row in range(n):
        new_row = list(input())
        lair.append(new_row)
        if "S" in new_row:
            position = row, new_row.index("S")
        elif 'B' in new_row:
            burrows.append((row, new_row.index("B")))
    return lair, burrows, position


def moving(start_pos, n, direct, lair, burrows):
    r, c = start_pos

    directions = {'right': (0, +1), 'left': (0, -1), 'up': (-1, 0), 'down': (+1, 0)}
    r, c = r + directions[direct][0], c + directions[direct][1]

    if is_valid(r, c, n):
        if lair[r][c] == "B":
            lair[r][c] = '.'
            burrows.remove((r, c))

            r, c = burrows[0]

            burrows.pop()
            return start_pos, (r, c)
        return start_pos, (r, c)
    else:
        return start_pos, None


def drawing_lair(old_pos, new_pos, lair):
    curr_food = 0

    r, c = old_pos
    if not new_pos:
        lair[r][c] = '.'
        return lair, curr_food

    row, col = new_pos

    if lair[row][col] == "*":
        curr_food += 1

    elif lair[row][col] == 'B':

        lair[r][c] = '.'
        lair[row][col] = '.'
        return lair, curr_food

    lair[r][c] = '.'

    return lair, curr_food


lair_size = int(input())
lair, burrows, start_position = fill_lair(lair_size)
position = start_position
lair = lair
food = 0
game_over = False

while food < 10:
    direction = input()
    old_cord, new_cord = moving(position, lair_size, direction, lair, burrows)
    if not new_cord:
        game_over = True
        lair = drawing_lair(old_cord, new_cord, lair)[0]
        break

    lair = drawing_lair(old_cord, new_cord, lair)[0]
    position = new_cord
    food += int(drawing_lair(old_cord, new_cord, lair)[1])

if game_over:
    print("Game over!")
else:
    lair[position[0]][position[1]] = 'S'
    print("You won! You fed the snake.")
print(f"Food eaten: {food}")
[print(*r, sep="") for r in lair]
