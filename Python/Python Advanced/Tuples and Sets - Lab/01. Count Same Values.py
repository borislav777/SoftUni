numbers = tuple(map(float, input().split()))

count_value = {}

for number in numbers:
    count_value[number] = numbers.count(number)

for number,count in count_value.items():
    print(f"{number} - {count} times")
