from collections import deque

row, col = [int(el) for el in input().split()]
word = deque(input())
matrix = [['0' for _ in range(col)] for _ in range(row)]

for row_i in range(row):

    for col_i in range(col):
        curr_char = word.popleft()
        matrix[row_i][col_i] = curr_char
        word.append(curr_char)

for i in range(len(matrix)):
    if i % 2 == 1:
        matrix[i].reverse()
    print(''.join(matrix[i]))
