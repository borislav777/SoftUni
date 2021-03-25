data = input().split()
products = {}
searched = input().split()
for index in range(0, len(data), 2):
    products[data[index]] = int(data[index + 1])
for searched_word in searched:
    if searched_word in products.keys():
        print(f"We have {products[searched_word]} of {searched_word} left")
    else:
        print(f"Sorry, we don't have {searched_word}")