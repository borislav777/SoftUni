def loading_bar(num1):
    bar = [".", ".", ".", ".", ".", ".", ".", ".", ".", "."]
    load = num1 // 10
    for index in range(load):
        bar[index] = "%"
    return bar


number = int(input())
if loading_bar(number).count("%") == 10:
    print("100% Complete!")
    print(f"[{''.join(loading_bar(number))}]")
else:
    print(f"{number}% [{''.join(loading_bar(number))}]")
    print("Still loading...")
