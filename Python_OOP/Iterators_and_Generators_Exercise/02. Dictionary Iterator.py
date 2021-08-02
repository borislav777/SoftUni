class dictionary_iter:

    def __init__(self, seq):
        self.seq = list(seq.items())
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.seq):
            raise StopIteration

        indx = self.index
        self.index += 1
        return self.seq[indx]


result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


