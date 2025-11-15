from Python.helpers import find_proper_divisors_of_n
from Python.timer import timer


def d(n: int) -> int:
    return sum(find_proper_divisors_of_n(n))


@timer
def p021(limit: int = 10_000) -> int:
    amicable_sum = 0
    for a in range(1, limit + 1):
        b = d(a)
        if d(b) == a and a != b:
            amicable_sum += a

    return amicable_sum


p021()
