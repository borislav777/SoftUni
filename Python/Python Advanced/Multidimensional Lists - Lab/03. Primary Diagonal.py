size_of_square = int(input())
matrix = [[int(el) for el in input().split()]for _ in range(size_of_square)]
sum_diagonal = 0
for d in range(size_of_square):
    sum_diagonal += matrix[d][d]

print(sum_diagonal)
