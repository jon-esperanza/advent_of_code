import time

""" Decorator to time a function (milliseconds) and print the result """


def timed(func, print_result=True):
    def wrapper(*args, **kwargs):
        start = current_milli_time()
        res = func(*args, **kwargs)
        end = current_milli_time()
        print(f"{func.__name__}")
        if print_result:
            print(f"\tResult: {res}")
        print(f"\tTotal time taken: {end - start}ms")
        return res

    return wrapper


def current_milli_time():
    return round(time.time() * 1000)
