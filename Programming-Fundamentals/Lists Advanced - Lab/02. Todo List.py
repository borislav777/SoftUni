notes = input()
to_do_list = [0] * 10
while not notes == "End":
    importance, value = notes.split("-")
    importance = int(importance) - 1
    to_do_list[importance] = value
    notes = input()
# to_do_list = [el for el in to_do_list if not el == 0]
to_do_list = list(filter(lambda el: not el == 0, to_do_list))
print(to_do_list)
