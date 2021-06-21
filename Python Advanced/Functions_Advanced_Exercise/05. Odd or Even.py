def odd_or_even(comm, seq):
    if comm == "Odd":
        sum_odd = sum([el for el in seq if el % 2 != 0])
        print(sum_odd*len(seq))
    else:
        sum_even = sum([el for el in seq if el % 2 == 0])
        print(sum_even * len(seq))


command = input()
numbers = list(map(int, input().split()))
odd_or_even(command,numbers)
