n = int(input())
matrix = [[int(el) for el in input().split()] for _ in range(n)]
first = 0
second = 0
col = n - 1
for index in range(n):
    first += matrix[index][index]
    second += matrix[index][col]
    col -= 1
print(abs(first - second))
