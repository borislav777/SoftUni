def vowel_filter(function):
    def wrapper():
        f = function()
        return [el for el in f if el in "aeoui"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
