def combination(names, chairs, curr_names=[]):
    if len(curr_names) == chairs:
        print(', '.join(curr_names))
        return
    for i in range(len(names)):
        curr_names.append(names[i])
        combination(names[i + 1:], chairs, curr_names)
        curr_names.pop()


data = input().split(", ")
number_chairs = int(input())
combination(data,number_chairs)
