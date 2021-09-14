def check_i_is_valid(r, c):
    if r in range(len(matrix)) and c in range(len(matrix)):
        return True
    return print("Invalid coordinates")


n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
command = input()
while not command == "END":
    manipulation = command.split()[0]
    row, col, value = [int(el) for el in command.split()[1::]]

    if check_i_is_valid(row, col):
        if manipulation == "Add":
            matrix[row][col] += value
        else:
            matrix[row][col] -= value
    command = input()
[print(*m) for m in matrix]
