from Python.timer import timer


def num_divisors(n: int) -> int:
    divisors = 0

    x = 1
    while x * x <= n:
        if n % x == 0:
            divisors += (1 if x * x == n else 2)
        x += 1

    return divisors


@timer
def p012(more_than_n_divisors: int) -> int:
    triangle_number = 0
    n = 1

    while num_divisors(triangle_number) <= more_than_n_divisors:
        triangle_number += n
        n += 1

    return triangle_number


p012(500)
