start_string = input()
aim_mutated_word = input()
result = ""
previous_result = start_string

for index_1 in range(len(start_string)):
    for index_2 in range(index_1 + 1):
        result += aim_mutated_word[index_2]
    for index_3 in range(index_1 + 1, len(start_string)):
        result += start_string[index_3]
    if not result == previous_result:
        print(result)
    previous_result = result
    result = ""
