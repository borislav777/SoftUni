data = input()

counter = {}
for el in data:
    if el not  in counter:
        counter[el] = data.count(el)

for chr1,count in sorted(counter.items()):
    print(f'{chr1}: {count} time/s')