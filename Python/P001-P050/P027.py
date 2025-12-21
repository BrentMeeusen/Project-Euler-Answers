from Python.helpers import is_prime
from Python.timer import timer


def f(a: int, b: int):
    return lambda n: (n * n) + (a * n) + b


@timer
def p027() -> int:
    most_primes = {
        "most": 0,
        "a": 0,
        "b": 0
    }

    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            func = f(a, b)

            n = 0
            while True:
                x = func(n)
                if x >= 2 and is_prime(x):
                    n += 1
                else:
                    break

            if n > most_primes["most"]:
                most_primes["most"] = n
                most_primes["a"] = a
                most_primes["b"] = b

    return most_primes["a"] * most_primes["b"]


p027()
