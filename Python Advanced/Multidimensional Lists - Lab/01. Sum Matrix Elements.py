rows, col = [int(el) for el in input().split(", ")]
matrix = []
sum_matrix = 0
for row in range(rows):
    matrix.append([int(el) for el in input().split(", ")])
    sum_matrix += sum(matrix[row])
print(sum_matrix)
print(matrix)