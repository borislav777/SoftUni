def all_permutations(seq):
    if len(seq) == 0:
        return []
    elif len(seq) == 1:
        return [seq]
    result = []
    for i in range(len(seq)):
        curr_el = seq[i]
        other_el = seq[:i] + seq[i + 1:]
        for el in all_permutations(other_el):
            result.append([curr_el] + el)
    return result


def possible_permutations(seq):
    perm = all_permutations(seq)
    for p in perm:
        yield p


[print(n) for n in possible_permutations([1, 2, 3])]
