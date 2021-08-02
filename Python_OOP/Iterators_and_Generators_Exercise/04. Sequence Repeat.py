class sequence_repeat:

    def __init__(self, seq, number):
        self.seq = seq
        self.number = number
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= 0:
            raise StopIteration

        idx = self.index
        self.number -= 1

        self.index += 1

        return self.seq[idx % len(self.seq)]


result = sequence_repeat('abc', 5)
for item in result:
    print(item, end='')
