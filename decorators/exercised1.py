def logged(func):
    def wrapper(*args, **kwargs):

        print(f"you called func{args}")
        returned_value = func(*args, **kwargs)
        print(f"it returned: {returned_value}")
        return print(returned_value)

    return wrapper


@logged
def func(*args):
    return 3 + len(args)
