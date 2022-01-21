class Integer:

    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(int(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000, 'IV': 4, 'IX': 9, 'XL': 40, 'XC': 90,
                 'CD': 400, 'CM': 900}
        i = 0
        num = 0
        while i < len(value):
            if i + 1 < len(value) and value[i:i + 2] in roman:
                num += roman[value[i:i + 2]]
                i += 2
            else:
                # print(i)
                num += roman[value[i]]
                i += 1
        return cls(num)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            try:
                value = int(value)
                return cls(value)
            except ValueError:
                print('wrong type')
        return 'wrong type'
