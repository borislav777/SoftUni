players = input().split(', ')
players_stats = {name: {'points': 501, 'throws': 0} for name in players}

matrix = [input().split() for _ in range(7)]
coordinates = input()

while len(coordinates) > 0:

    row, col = tuple(map(int, coordinates.lstrip("(").rstrip(")").split(", ")))
    curr_player = players[0]

    players_stats[curr_player]['throws'] += 1
    if row in range(len(matrix)) and col in range(len(matrix)):
        curr_position = matrix[row][col]
        if curr_position == 'B':
            print(f"{curr_player} won the game with {players_stats[curr_player]['throws']} throws!")
            break

        elif curr_position == 'D' or curr_position == 'T':
            mapper = {'D': 2, 'T': 3}
            points = (int(matrix[row][0]) + int(matrix[row][len(matrix) - 1]) + int(matrix[0][col]) + int(
                matrix[len(matrix) - 1][col])) * int(mapper[curr_position])
            players_stats[curr_player]['points'] -= points

        elif curr_position.isdigit():
            players_stats[curr_player]['points'] -= int(curr_position)

        if players_stats[curr_player]['points'] <= 0:
            print(f"{curr_player} won the game with {players_stats[curr_player]['throws']} throws!")
            break
    players.reverse()
    coordinates = input()
