n = int(input())
matrix = [[int(el) for el in input().split(', ')] for _ in range(n)]
first = [matrix[row][row] for row in range(n)]
col = n -1
second = []
for row in range(n):
    second.append(matrix[row][col])
    col -= 1

print(f"First diagonal: {', '.join([str(el) for el in first])}. Sum: {sum(first)}")
print(f"Second diagonal: {', '.join([str(el) for el in second])}. Sum: {sum(second)}")

