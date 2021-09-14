text = input().split()
after_numbers = []
for num in text:
    after_numbers.append(int(num) * -1)
print(after_numbers)
