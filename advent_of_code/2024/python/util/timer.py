import time

""" Decorator to time a function and print the result """


def timed(func, print_result=True):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__}")
        if print_result:
            print(f"\tResult: {res}")
        print(f"\tTotal time taken: {end - start}")
        return res

    return wrapper
