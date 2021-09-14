def chr_to_ord(ch1, ch2):
    char = []
    start_chr = ord(ch1)
    end_chr = ord(ch2)
    for num in range(start_chr+1, end_chr):
        char.append(chr(num))
    return char


chr1 = input()
chr2 = input()
result = chr_to_ord(chr1, chr2)
print(" ".join(result))
