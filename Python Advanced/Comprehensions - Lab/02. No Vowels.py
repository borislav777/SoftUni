text = input()
vowels = ['a', 'o', 'u', 'e', 'i']
print(''.join([el for el in text if el.lower() not in vowels]))
