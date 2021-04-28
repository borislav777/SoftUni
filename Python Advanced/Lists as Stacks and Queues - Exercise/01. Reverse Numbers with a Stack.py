numbers = input().split()
reversed_stack = []
while numbers:
    reversed_stack.append(numbers.pop())
print(' '.join(reversed_stack))
