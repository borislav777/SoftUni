numbers = [int(num) for num in input().split()]
avg = sum(numbers) / len(numbers)
top_numbers = [num for num in numbers if num > avg]
top_numbers.sort(reverse=True)
filtered_numbers = []
il = [filtered_numbers.append(nums) for nums in top_numbers if len(filtered_numbers) < 5]

if len(top_numbers) == 0:
    print("No")
else:

    print(" ".join([str(el) for el in filtered_numbers]))
