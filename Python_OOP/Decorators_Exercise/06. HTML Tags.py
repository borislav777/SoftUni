def tags(t):
    def decorator(func):
        def wrapper(*args):
            f = func(*args)
            return f"<{t}>{f}</{t}>"

        return wrapper
    return decorator



@tags('h1')
def to_upper(text):
    return text.upper()
print(to_upper('hello'))