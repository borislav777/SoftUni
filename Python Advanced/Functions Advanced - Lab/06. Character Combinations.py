def chr_combinations(string, index=0):
    if index >= len(string):
        print(''.join(string))
        return
    chr_combinations(string, index + 1)
    for i in range(index + 1, len(string)):
        string[index], string[i] = string[i], string[index]
        chr_combinations(string, index + 1)
        string[index], string[i] = string[i], string[index]


text = list(input())
chr_combinations(text)
