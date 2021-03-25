numbers = [int(num) for num in input().split(", ")]

even_number = [index for index in range(len(numbers)) if numbers[index] % 2 == 0]
print(even_number)
