number_lines = int(input())
for first in range(97, 97 + number_lines):
    chr_1 = chr(first)
    for second in range(97, 97 + number_lines):
        chr_2 = chr(second)
        for third in range(97, 97 + number_lines):
            chr_3 = chr(third)
            print(chr_1+chr_2+chr_3)
