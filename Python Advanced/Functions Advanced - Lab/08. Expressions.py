def expression(numbers, curr_express='', sum_express=0):
    if not numbers:
        print(f"{curr_express}={sum_express}")
        return

    expression(numbers[1:], curr_express + '+1', sum_express + 1)
    expression(numbers[1:], curr_express + '-1', sum_express - 1)


data = list(map(int, input().split(', ')))
expression(data)
