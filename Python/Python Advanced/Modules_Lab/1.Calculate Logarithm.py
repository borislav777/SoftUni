from math import log


def calculate_logarithm(num, b):
    if base == 'natural':
        return print(f"{log(num):.2f}")
    print(f"{log(num, int(b)):.2f}")


number = int(input())
base = input()
calculate_logarithm(number, base)
