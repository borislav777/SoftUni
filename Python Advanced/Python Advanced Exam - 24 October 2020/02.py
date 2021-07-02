def is_valid(r, c, n):
    if 0 <= r < n and 0 <= c < n:
        return True
    return False


board = [input().split() for _ in range(8)]
result = []
directions = {
    'up': (-1, 0),
    'down': (+1, 0),
    'left': (0, -1),
    'right': (0, +1),
    'up-left': (-1, -1),
    'up-right': (-1, +1),
    'down-left': (+1, -1),
    'down-right': (+1, + 1)
}
for row in range(len(board)):
    for col in range(len(board)):
        if board[row][col] == 'Q':

            for direct in directions:
                new_row, new_col = row + directions[direct][0], col + directions[direct][1]
                while is_valid(new_row, new_col, len(board)):
                    if board[new_row][new_col] == 'K':
                        result.append([row, col])
                        break
                    elif board[new_row][new_col] == 'Q':
                        break
                    new_row += directions[direct][0]
                    new_col += directions[direct][1]
if not result:
    print("The king is safe!")
else:
    print(*result, sep='\n')

