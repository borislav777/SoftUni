def type_check(t):
    def decorator(function):
        def wrapper(num):
            if type(num) == t:
                return function(num)
            return "Bad Type"

        return wrapper

    return decorator


@type_check(str)
def first_letter(word):
    return word[0]


print(first_letter('Hello World'))
print(first_letter(['Not', 'A', 'String']))
