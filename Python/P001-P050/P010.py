from Python.helpers import find_primes_below_n
from Python.timer import timer


@timer
def p010(n: int) -> int:
    return sum(find_primes_below_n(n))


p010(2_000_000)
