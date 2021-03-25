sequence = [int(num) for num in input().split()]
command = input()
indexs = []
counter = 0
while not command == "End":
    target = int(command)
    if len(sequence) > target:
        if not sequence[target] in indexs:

            counter += 1

            for num in range(len(sequence)):
                if not num == target and not sequence[num] in indexs:
                    if sequence[num] > sequence[target]:
                        sequence[num] -= sequence[target]
                    elif sequence[num] <= sequence[target]:
                        sequence[num] += sequence[target]
            sequence[target] = -1
            indexs.append(sequence[target])

    command = input()

print(f"Shot targets: {counter} -> {' '.join(list([str(el) for el in sequence]))}")
