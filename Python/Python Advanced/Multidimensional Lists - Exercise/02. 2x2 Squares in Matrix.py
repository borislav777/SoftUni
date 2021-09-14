row, col = [int(el) for el in input().split()]
matrix = [input().split() for _ in range(row)]
counter = 0
for row_i in range(row-1):
    for col_i in range(col-1):
        if matrix[row_i][col_i] == matrix[row_i][col_i + 1] and matrix[row_i + 1][col_i] == matrix[row_i + 1][col_i + 1] and matrix[row_i][col_i] == matrix[row_i+1][col_i] and matrix[row_i][col_i+1] == matrix[row_i+1][col_i+1]:
            counter += 1
print(counter)