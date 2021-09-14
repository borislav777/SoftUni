from math import floor


def is_valid(mat, r, c):
    if r in range(len(mat)) and c in range(len(mat)):
        return True
    return False


n = int(input())
matrix = [input().split() for _ in range(n)]
coins = 0
positions = []
start_position = None
mapper = {'right': (0, +1), 'left': (0, -1), 'up': (-1, 0), 'down': (+1, 0)}
game_lost = False
for r in range(len(matrix)):
    for c in range(len(matrix)):
        if matrix[r][c] == "P":
            start_position = r, c
            break
while coins < 100:
    command = input()
    if command in mapper:
        row, col = start_position
        row_cord, col_cord = mapper[command]
        new_rol = row + row_cord
        new_col = col + col_cord

        if is_valid(matrix, new_rol, new_col):

            if matrix[new_rol][new_col] == "X":
                game_lost = True
                coins = floor(coins / 2)
                break

            coins += int(matrix[new_rol][new_col])
            positions.append([new_rol, new_col])
            start_position = new_rol, new_col

        else:
            game_lost = True
            coins = floor(coins / 2)
            break

if not game_lost:
    print(f"You won! You've collected {floor(coins)} coins.")

else:
    print(f"Game over! You've collected {floor(coins)} coins.")

print("Your path: ")
print(*positions, sep="\n")
