def expression(numbers, curr_express='', sum_express=0):
    if not numbers:
        print(f"{curr_express}={sum_express}")
        return

    expression(numbers[1:], curr_express + f'+{numbers[0]}', sum_express + numbers[0])
    expression(numbers[1:], curr_express + f'-{numbers[0]}', sum_express - numbers[0])


data = list(map(int, input().split(', ')))
expression(data)
