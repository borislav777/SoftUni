expression = input()
stack = []
for i in range(len(expression)):
    if expression[i] == "(":
        stack.append(i)
    elif expression[i] == ")":
        start = stack.pop()
        print(expression[start:i+1])
