def generate_numbers(n):
    seq = [0, 1]

    for i in range(n - 2):
        seq.append(seq[i] + seq[i + 1])
    return seq


def locate_number(n, seq):
    for i in range(len(seq)):
        if seq[i] == n:
            return print(f"The number - {n} is at index {i}")
    return print(f"The number {n} is not in the sequence")
