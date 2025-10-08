import functools
from time import perf_counter_ns
from typing import Any


def timer(func):
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> Any:
        start = perf_counter_ns()
        result = func(*args, **kwargs)
        end = perf_counter_ns()

        print(result)
        print(f"{func.__name__} took {(end - start) / 1_000_000:0.4f} ms")
        return result

    return wrapper
