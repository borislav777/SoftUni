def multiply(n):
    def decorator(func):
        def wrapper(num):
            f = func(num)
            return f * n

        return wrapper

    return decorator

@multiply(5)
def add_ten(number):
    return number + 10

print(add_ten(6))

