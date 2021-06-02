rows, cols = [int(el) for el in input().split(", ")]
matrix = []
for _ in range(rows):
    matrix.append([int(el) for el in input().split()])

for col in range(cols):
    sum_rows = 0
    for row in range(rows):
        sum_rows += matrix[row][col]
    print(sum_rows)