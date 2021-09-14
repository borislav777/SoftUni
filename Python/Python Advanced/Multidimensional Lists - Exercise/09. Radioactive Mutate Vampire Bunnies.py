def check_is_valid(r, c):
    if r in range(rows) and c in range(cols):
        return True
    return False


rows, cols = [int(el) for el in input().split()]
matrix = [list(input()) for el in range(rows)]
commands = list(input())
position = None
bunny_direct = [(-1, 0), (+1, 0), (0, -1), (0, +1)]
p_direct = {'U': (-1, 0), 'D': (+1, 0), 'L': (0, -1), 'R': (0, +1)}
is_dead = False
is_win = False

for row_i in range(rows):
    for col_i in range(cols):

        if matrix[row_i][col_i] == "P":
            position = row_i, col_i

for command in commands:
    if is_win or is_dead:
        break
    curr_row, curr_col = position
    curr_row += p_direct[command][0]
    curr_col += p_direct[command][1]
    if check_is_valid(curr_row, curr_col):
        if matrix[curr_row][curr_col] == 'B':
            is_dead = True
            position = curr_row, curr_col
        else:
            matrix[curr_row][curr_col] = 'P'
            matrix[position[0]][position[1]] = '.'
            position = curr_row, curr_col
    else:
        matrix[position[0]][position[1]] = '.'
        is_win = True

    bunny_cord = []
    for row_i in range(rows):
        for col_i in range(cols):

            if matrix[row_i][col_i] == 'B':
                for dir_row, dir_col in bunny_direct:
                    next_row = row_i + dir_row
                    next_col = col_i + dir_col
                    if check_is_valid(next_row, next_col):
                        if matrix[next_row][next_col] == "P":
                            is_dead = True

                        bunny_cord.append((next_row, next_col))

    for b_r, b_c in bunny_cord:
        matrix[b_r][b_c] = 'B'

[print(''.join(matrix[i])) for i in range(len(matrix))]

if is_win:
    print(f"won: {position[0]} {position[1]}")
else:
    print(f"dead: {position[0]} {position[1]}")
