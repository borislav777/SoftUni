def negative_vs_positive(seq):
    positive = sum([el for el in seq if el > 0])
    negative = sum([el for el in seq if el < 0])
    print(negative)
    print(positive)

    if positive > abs(negative):
        print("The positives are stronger than the negatives")
    else:
        print("The negatives are stronger than the positives")


numbers = list(map(int, input().split()))
negative_vs_positive(numbers)
