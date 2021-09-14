def even_numbers(seq):
    return list(filter(lambda x: x % 2 == 0, seq))


numbers = map(int, input().split())
print(even_numbers(numbers))
