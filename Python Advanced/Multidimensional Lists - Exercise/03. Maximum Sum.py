from sys import maxsize

row, col = [int(el) for el in input().split()]
matrix = [[int(el) for el in input().split()] for _ in range(row)]
max_sum = - maxsize
sub_matrix = []
for row_i in range(row - 2):
    for col_i in range(col - 2):
        curr_matrix = [[matrix[row_i][col_i], matrix[row_i][col_i + 1], matrix[row_i][col_i + 2]], [matrix[row_i + 1][col_i], matrix[row_i + 1][col_i + 1], matrix[row_i + 1][col_i + 2]], [matrix[row_i + 2][col_i], matrix[row_i + 2][col_i + 1], matrix[row_i + 2][col_i + 2]] ]
        curr_sum = sum([sum(el) for el in curr_matrix])
        if curr_sum >= max_sum:
            max_sum = curr_sum
            sub_matrix = curr_matrix

print(f"Sum = {max_sum}")
for i in range(len(sub_matrix)):
    print(*sub_matrix[i])