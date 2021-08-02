def fibonacci():
    first_num = 0
    second_num = 1

    yield first_num
    yield second_num
    first_number = second_num
    second_number = first_num
    while True:
        fn = first_number + second_number
        yield fn
        second_number = first_number
        first_number = fn


generator = fibonacci()
for i in range(5):
    print(next(generator))
