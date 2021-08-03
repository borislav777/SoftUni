import time


def exec_time(function):
    def wrapper(*args):
        start = time.time()
        function(*args)
        end = time.time()
        return end - start

    return wrapper


@exec_time
def concatenate(strings):
    result = ""
    for string in strings:
        result += string
    return result
print(concatenate(["a" for i in range(1000000)]))
