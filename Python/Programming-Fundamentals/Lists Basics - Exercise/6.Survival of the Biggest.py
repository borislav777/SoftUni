numbers = input().split()
new_numbers = [int(i) for i in numbers]
numbers_remove = int(input())

for number in range(numbers_remove):
    new_numbers.remove(min(new_numbers))
print(new_numbers)
