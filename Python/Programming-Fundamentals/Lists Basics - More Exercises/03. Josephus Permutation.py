string_permutation = input().split()

k = int(input())
new = []

counter = 0
index_1 = 0
while string_permutation:

    counter += 1

    if counter % k == 0:
        new.append(string_permutation[index_1])
        string_permutation.pop(index_1)

    else:
        index_1 += 1

    if index_1 >= len(string_permutation):
        index_1 = 0

print(str(new).replace(' ', '').replace('\'', ''))
