command = input()
coffee = 0
words = ["dog", "cat", "movie", "coding", "DOG", "CAT", "MOVIE", "CODING"]
while not command == "END":
    for word in words:
        if command == word:
            if command.isupper():
                coffee += 2
            elif command.islower():
                coffee += 1

    command = input()
if coffee > 5:
    print("You need extra sleep")

else:
    print(coffee)
