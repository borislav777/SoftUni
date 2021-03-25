string = input()
string_2 = input()

result = ""
previous_result =string

for index in range(len(string_2)):
    x = slice(index + 1)
    y = slice(index + 1, len(string))
    result += string_2[x] + string[y]
    if not result == previous_result:
        print(result)
    previous_result=result
    result = ""