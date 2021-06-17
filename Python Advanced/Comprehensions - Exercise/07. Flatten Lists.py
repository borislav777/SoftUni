data = input().split("|")[::-1]

result = [el for i in range(len(data)) for el in data[i].split()]
print(*result)
