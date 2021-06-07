n = int(input())

board = [list(input()) for _ in range(n)]
moves = [(-2, -1), (-2, 1), (1, 2), (1, -2), (2, -1), (2, 1), (-1, -2), (-1, 2)]


counter = 0
kills = 0

while True:
    max_kills = 0

    killer_position = []
    for row in range(n):
        for col in range(n):
            if board[row][col] == 'K':
                kills = 0
                for i in range(len(moves)):
                    r, c = moves[i]
                    if r + row in range(len(board)) and c + col in range(len(board)):

                        if board[row + r][col + c] == 'K':
                            kills += 1

                if kills > max_kills:
                    max_kills = kills

                    killer_position = [row, col]

    if killer_position:
        board[killer_position[0]][killer_position[1]] = '0'
        counter += 1
    else:
        break

print(counter)
