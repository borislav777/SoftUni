class custom_range:

    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        curr_num = self.start
        self.start += 1
        return curr_num


one_to_ten = custom_range(1, 10)
for num in one_to_ten:
    print(num)