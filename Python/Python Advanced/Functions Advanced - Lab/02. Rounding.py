def round_num_on_seq(seq):
    return [round(num) for num in seq]


numbers = map(float, input().split())
print(round_num_on_seq(numbers))
