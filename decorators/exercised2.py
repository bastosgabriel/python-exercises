
def cache(func):
    def wrapper(n):
        result_dict[str(n)] = func(n)
        print(result_dict)
        return func(n)

    return wrapper


result_dict = {}

@cache
def fibonacci(n):
    assert n >= 0
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(5))