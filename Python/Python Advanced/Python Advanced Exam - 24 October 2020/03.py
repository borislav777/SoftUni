from collections import deque


def best_list_pureness(seq, k):
    seq = deque(seq)
    data = {}
    best_pureness = None
    max_pureness = 0

    for r in range(k + 1):

        if r > len(seq):
            break

        sum_pureness = sum([i * n for i, n in enumerate(seq)])
        seq.appendleft(seq.pop())
        if sum_pureness > max_pureness:
            max_pureness = sum_pureness
            best_pureness = r, sum_pureness
    return f"Best pureness {best_pureness[1]} after {best_pureness[0]} rotations"


test = ([7, 9, 2, 5, 3, 4], 3)
result = best_list_pureness(*test)
print(result)
