text = input()
counter = {}
for chr1 in text:
    if chr1 == " ":
        continue
    else:
        if chr1 not in counter:
            counter[chr1] = 1
        else:
            counter[chr1] += 1

for chr2, count in counter.items():
    print(f"{chr2} -> {count}")
