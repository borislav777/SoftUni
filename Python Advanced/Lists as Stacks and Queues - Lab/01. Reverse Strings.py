text = input()
stack = []
for chr in text:
    stack.append(chr)
for i in range(len(stack)):
    print(stack.pop(),end="")
