def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


initial_string = input()
matrix_size = int(input())
matrix = []
position = None
directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'right': (0, +1),
    'left': (0, -1)
}
for r in range(matrix_size):
    curr_row = input()
    matrix.append(list(curr_row))
    if 'P' in curr_row:
        position = r, curr_row.index('P')
number_command = int(input())

for _ in range(number_command):
    command = input()
    new_row = position[0] + directions[command][0]
    new_col = position[1] + directions[command][1]

    if is_valid(new_row, new_col, matrix_size):
        matrix[position[0]][position[1]] = '-'
        if matrix[new_row][new_col].isalpha():
            initial_string += matrix[new_row][new_col]
            matrix[new_row][new_col] = 'P'
        position = new_row,new_col
    else:
        initial_string = initial_string[:len(initial_string)-1]

print(initial_string)
[print(''.join(m)) for m in matrix]