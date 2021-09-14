parentheses = input()
stack = []
mapper = {'{': '}', '(': ')', '[': ']'}
is_balanced = True
for p in parentheses:
    if p in "{([":
        stack.append(p)
    else:
        if not stack:
            is_balanced = False
            break
        curr_parentheses = stack.pop()
        if not mapper[curr_parentheses] == p:
            is_balanced = False
            break
if is_balanced:
    print("YES")
else:
    print("NO")
