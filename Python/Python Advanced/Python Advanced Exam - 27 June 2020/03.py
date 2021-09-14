from collections import deque


def list_manipulator(seq, *args):
    seq = deque(seq)

    if args[0] == "add":
        if args[1] == "beginning":
            for num in range(len(args)-1, 1, -1):
                seq.appendleft(args[num])
            return list(seq)
        elif args[1] == "end":
            for num in args[2:]:
                seq.append(int(num))
            return list(seq)
    elif args[0] == "remove":
        if args[1] == "beginning":
            if len(args) > 2:
                for _ in range(int(args[2])):
                    seq.popleft()
            else:
                seq.popleft()
            return list(seq)

        elif args[1] == "end":
            if len(args) > 2:
                for _ in range(int(args[2])):
                    seq.pop()

            else:
                seq.pop()
            return list(seq)


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1, 2, 3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))
