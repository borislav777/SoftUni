class EncryptionGenerator:

    def __init__(self, text):
        self.text = text

    def __add__(self, other):
        result = ''
        if isinstance(other, int):
            for letter in self.text:
                new_symbol = ord(letter) + other
                while new_symbol < 32:
                    new_symbol += 95
                while new_symbol > 126:
                    new_symbol -= 95
                result += chr(new_symbol)
            return result
        raise ValueError("You must add a number.")

example = EncryptionGenerator('Super-Secret Message')
print(example + 20)
print(example + (-52))
