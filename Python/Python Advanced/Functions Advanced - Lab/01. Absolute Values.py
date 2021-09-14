def abs_on_sequence(seq):
    return [abs(el) for el in seq]


numbers = map(float, input().split())
print(abs_on_sequence(numbers))
