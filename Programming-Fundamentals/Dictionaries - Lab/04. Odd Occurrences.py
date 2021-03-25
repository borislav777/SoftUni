words = input().split()
dict = {}
for word in words:
    word = word.lower()
    if word not in dict:
        dict[word] = 1
    else:
        dict[word] += 1

for key, value in dict.items():
    if not value % 2 == 0:
        print(f"{key}", end=" ")
