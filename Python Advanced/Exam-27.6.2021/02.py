def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


position = None
matrix = []
shooting = []
target_count = 0
for row in range(5):
    curr_row = input().split()
    matrix.append(curr_row)
    if 'A' in curr_row:
        position = row, curr_row.index('A')
    if 'x' in curr_row:
        target_count += curr_row.count('x')

number_commands = int(input())
for _ in range(number_commands):

    command = input()
    curr_command = command.split()[0]

    if curr_command == "move":
        direction = command.split()[1]
        steps = int(command.split()[2])
        move_directions = {
            'right': [0, +steps],
            'left': [0, -steps],
            'up': [-steps, 0],
            'down': [+steps, 0]
        }
        row, col = position
        new_row, new_col = row + move_directions[direction][0], col + move_directions[direction][1]
        if is_valid(new_row, new_col, len(matrix)):
            if matrix[new_row][new_col] == '.':
                position = new_row, new_col

    elif curr_command == "shoot":
        direction = command.split()[1]
        s_directions = {
            'right': (0, +1),
            'left': (0, -1),
            'up': (-1, 0),
            'down': (+1, 0)
        }
        row, col = position
        new_row, new_col = row + s_directions[direction][0], col + s_directions[direction][1]
        while is_valid(new_row, new_col, len(matrix)):

            if matrix[new_row][new_col] == 'x':
                shooting.append([new_row, new_col])
                matrix[new_row][new_col] = '.'
                target_count -= 1
                break
            new_row += s_directions[direction][0]
            new_col += s_directions[direction][1]
    if target_count <= 0:
        break

if target_count <= 0:
    print(f"Training completed! All {len(shooting)} targets hit.")
else:
    print(f"Training not completed! {target_count} targets left.")
if shooting:
    print(*shooting, sep='\n')
