n = int(input())
matrix = [list(input()) for _ in range(n)]
symb = input()
position = None
for row in range(n):
    for col in range(n):
        if matrix[row][col] == symb:
            position = (row, col)
            break
    if position:
        break
if position:
    print(position)

else:
    print(f"{symb} does not occur in the matrix")


