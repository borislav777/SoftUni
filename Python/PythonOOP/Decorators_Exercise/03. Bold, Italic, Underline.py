def make_bold(function):
    def wrapper(*args):
        f = function(*args)
        return f"<b>{f}</b>"

    return wrapper


def make_italic(function):
    def wrapper(*args):
        f = function(*args)
        return f"<i>{f}</i>"

    return wrapper


def make_underline(function):
    def wrapper(*args):
        f = function(*args)
        return f"<u>{f}</u>"

    return wrapper


@make_bold
@make_italic
@make_underline
def greet_all(*args):
    return f"Hello, {', '.join(args)}"

print(greet_all("Peter", "George"))
