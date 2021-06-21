def min_max_sum_numbers(seq):
    print(f"The minimum number is {min(seq)}")
    print(f"The maximum number is {max(seq)}")
    print(f"The sum number is: {sum(seq)}")


numbers = list(map(int, input().split()))
min_max_sum_numbers(numbers)
