n, m = [int(el) for el in input().split()]
first_set = {input() for _ in range(n)}
second_set = {input() for _ in range(m)}
first_set = first_set.intersection(second_set)
for el in first_set:
    print(el)
