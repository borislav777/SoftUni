class vowels:

    def __init__(self, text):
        self.text = text
        self.vowels = ['a', 'e', 'i', 'u', 'y', 'o', ]
        self.vowels_in_text = [el for el in self.text if el.lower() in self.vowels]
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.vowels_in_text):
            raise StopIteration
        inx = self.index
        self.index += 1
        return self.vowels_in_text[inx]


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)

