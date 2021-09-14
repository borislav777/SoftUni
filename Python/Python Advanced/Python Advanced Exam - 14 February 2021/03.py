from collections import deque


def stock_availability(box, command, *args):
    boxes = deque(box)
    if command == "delivery":
        for b in args:
            boxes.append(b)
    elif command == "sell":
        if args:
            for el in args:
                if isinstance(el, int):
                    for _ in range(int(el)):
                        boxes.popleft()
                elif el in boxes:
                    while el in boxes:
                        boxes.remove(el)
        else:
            boxes.popleft()
    return list(boxes)

print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))

