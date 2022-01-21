class reverse_iter:

    def __init__(self, seq):
        self.seq = seq
        self.start = len(seq) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.end:
            raise StopIteration
        inx = self.start
        self.start -= 1
        return self.seq[inx]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)


