text = input().split()

if text[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:

    for elements in text:

        if elements == "wolf,":
            a = text.index("wolf,")

            print(f"Oi! Sheep number {len(text) - a-1} ! You are about to be eaten by a wolf!")
            break
