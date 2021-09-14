rol, col = [int(el) for el in input().split()]
matrix = [[f"{chr(97 + row)}{chr(97 + row + col)}{chr(97 + row)}" for col in range(col)] for row in range(rol)]
[print(*m,sep=" ") for m in matrix]
