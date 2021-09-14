import sys

numbers = int(input())
odd_sum = 0
odd_min = sys.maxsize
odd_max = -sys.maxsize
even_min = sys.maxsize
even_max = -sys.maxsize
even_sum = 0

for position in range(1, numbers + 1):
    value = float(input())
    if position % 2 == 0:
        even_sum += value
        if even_min > value:
            even_min = value
        if even_max < value:
            even_max = value

    else:
        odd_sum += value
        if odd_min > value:
            odd_min = value
        if odd_max < value:
            odd_max = value

print(f"OddSum={odd_sum:.2f},")
if odd_min == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={odd_min:.2f},")
if odd_max == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={odd_max:.2f},")

print(f"EvenSum={even_sum:.2f},")
if even_min == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={even_min:.2f},")
if even_max == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={even_max:.2f}")
