searched_book = input()
another_book = input()
count_book = 0
isFounded = False

while another_book != "No More Books":

    if searched_book == another_book:
        isFounded = True
        break
    count_book += 1
    another_book = input()
if isFounded:
    print(f"You checked {count_book} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {count_book} books.")
