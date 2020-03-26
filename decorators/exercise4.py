'''
Make a decorator to re-execute a function if it returns False. If False is returned 10 times the decorator should give up

'''

import time


def retry(tries):
    def decorator(function):
        def wrapper(arg):
            for n in range(tries):
                returned_value = function(arg)
                if (returned_value == True):
                    print(f"{n+1} try: Success")
                    return returned_value
                else:
                    print(f"{n+1} try: Failed")
                    time.sleep(2)
                    continue
            print(f"The function failed {n} times")
        return wrapper
    return decorator


tries = 10

@retry(tries)
def bollean_function(parameter: bool) -> bool:
    return parameter


print(bollean_function(False))