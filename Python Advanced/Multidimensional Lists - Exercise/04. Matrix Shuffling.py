row, col = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(row)]

command = input()

while not command == "END":

    if command.startswith("swap") and len(command.split()) == 5:
        row_1, col_1, row_2, col_2 = [int(el) for el in command.split()[1:]]
        if row_1 in range(row) and row_2 in range(
            row) and col_1 in range(col) and col_2 in range(col):

            matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]
            for i in range(len(matrix)):
                print(*matrix[i])
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
    command = input()

