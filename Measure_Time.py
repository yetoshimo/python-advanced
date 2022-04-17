from functools import wraps
from time import time


def measure_time(func):
    @wraps(func)
    def wrapper(count):
        start = time()
        result = func(count)
        end = time()
        print(f'{func.__name__} executed in {end - start} seconds')
        return result

    return wrapper


@measure_time
def big_loop(counter: int):
    for i in range(counter):
        print(f"looping i")


big_loop(int(input()))
