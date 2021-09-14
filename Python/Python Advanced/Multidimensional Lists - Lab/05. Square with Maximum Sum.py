import sys

rows, columns = [int(el) for el in input().split(", ")]

matrix = [[int(el) for el in input().split(", ")] for _ in range(rows)]
max_sum = - sys.maxsize
position = None
for row in range(rows - 1, 0, -1):
    for col in range(columns - 1, 0, -1):
        curr_sum = matrix[row][col] + matrix[row][col - 1] + matrix[row - 1][col] + matrix[row - 1][col - 1]
        if curr_sum >= max_sum:
            max_sum = curr_sum
            position = (row, col)
row, col = position
print(matrix[row-1][col-1], matrix[row-1][col])
print(matrix[row][col-1], matrix[row][col])
print(max_sum)
