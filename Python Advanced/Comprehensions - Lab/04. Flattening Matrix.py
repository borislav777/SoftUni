n = int(input())

new_matrix = []
flattering_matrix = [new_matrix.extend(input().split(", ")) for _ in range(n)]
print([int(el) for el in new_matrix])


