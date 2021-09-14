def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


matrix_size = int(input())
matrix = [['-' for _ in range(matrix_size)] for _ in range(matrix_size)]
number_bombs = int(input())
bombs = [eval(input()) for _ in range(number_bombs)]
directions = [
    (-1, 0),
    (+1, 0),
    (0, -1),
    (0, +1),
    (+1, -1),
    (+1, +1),
    (-1, -1),
    (-1, +1)
]
for bomb in bombs:
    row, col = bomb
    matrix[row][col] = "*"
for r in range(matrix_size):
    for c in range(matrix_size):
        counter = 0
        if matrix[r][c] == '*':
            continue
        for direction in directions:
            new_rol, new_col = r + direction[0], c + direction[1]
            if is_valid(new_rol, new_col, matrix_size):
                if matrix[new_rol][new_col] == "*":
                    counter += 1
        matrix[r][c] = counter
[print(*m) for m in matrix]
