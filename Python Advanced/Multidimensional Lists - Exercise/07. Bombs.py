def check_is_valid(n, t_r, t_c):
    if t_r in range(n) and t_c in range(n):
        if matrix[t_r][t_c] > 0:
            return True
    return False


n = int(input())

matrix = [[int(el) for el in input().split()] for _ in range(n)]
coordinates = input().split()
alive_cells = 0
sum_cells = 0

for index in range(len(coordinates)):
    row, col = [int(el) for el in coordinates[index].split(",")]
    bomb = matrix[row][col]
    if bomb > 0:
        if check_is_valid(n, row, col - 1):
            left_target = matrix[row][col - 1] - bomb
            matrix[row][col - 1] = left_target
        if check_is_valid(n, row, col + 1):
            right_target = matrix[row][col + 1] - bomb
            matrix[row][col + 1] = right_target
        if check_is_valid(n, row - 1, col):
            upper_target = matrix[row - 1][col] - bomb
            matrix[row - 1][col] = upper_target
        if check_is_valid(n, row + 1, col):
            bottom_target = matrix[row + 1][col] - bomb
            matrix[row + 1][col] = bottom_target
        if check_is_valid(n, row - 1, col - 1):
            first_diagonal_target = matrix[row - 1][col - 1] - bomb
            matrix[row - 1][col - 1] = first_diagonal_target
        if check_is_valid(n, row + 1, col + 1):
            second_diagonal_target = matrix[row + 1][col + 1] - bomb
            matrix[row + 1][col + 1] = second_diagonal_target
        if check_is_valid(n, row - 1, col + 1):
            third_diagonal_target = matrix[row - 1][col + 1] - bomb
            matrix[row - 1][col + 1] = third_diagonal_target
        if check_is_valid(n, row + 1, col - 1):
            four_diagonal_target = matrix[row + 1][col - 1] - bomb
            matrix[row + 1][col - 1] = four_diagonal_target

        matrix[row][col] = 0
for w in range(n):
    for c in range(n):
        if matrix[w][c] > 0:
            sum_cells += matrix[w][c]
            alive_cells += 1
print(f"Alive cells: {alive_cells}")
print(f"Sum: {sum_cells}")
for i in range(len(matrix)):
    print(*matrix[i])