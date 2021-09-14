def check_is_valid(field, row, col):
    if row in range(len(field)) and col in range(len(field)):
        return True
    return False


n = int(input())
commands = input().split()
field = [input().split() for _ in range(n)]
position = None
coals = 0

for row_i in range(n):
    for col_i in range(n):
        if field[row_i][col_i] == 's':
            position = row_i, col_i
        elif field[row_i][col_i] == 'c':
            coals += 1

directions = {'right': +1, 'left': -1, 'up': -1, 'down': +1}
is_valid = True
for comm in commands:
    row, col = position
    if comm == "right" or comm == 'left':
        col += directions[comm]
    elif comm == 'up' or comm == 'down':
        row += directions[comm]
    if check_is_valid(field, row, col):
        position = row, col
        if field[row][col] == 'c':
            coals -= 1
            field[row][col] = '*'
            if coals <= 0:
                print(f"You collected all coals! ({row}, {col})")
                is_valid = False
                break

        elif field[row][col] == 'e':
            print(f"Game over! ({row}, {col})")
            is_valid = False
            break

if is_valid:
    print(f"{coals} coals left. ({position[0]}, {position[1]})")
