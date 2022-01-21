def even_numbers(function):
    def wrapper(num):
        f = function(num)
        return [num for num in f if num % 2 == 0]

    return wrapper


@even_numbers
def get_numbers(numbers):
    return numbers


print(get_numbers([1, 2, 3, 4, 5]))
