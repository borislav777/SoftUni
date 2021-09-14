data = input().split()

products = {}

for index in range(0, len(data), 2):
    products[data[index]] = int(data[index + 1])

print(products)