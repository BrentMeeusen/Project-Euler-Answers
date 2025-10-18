from Python.helpers import is_prime
from Python.timer import timer


@timer
def p007(nth_prime: int) -> int:
    if nth_prime == 1:
        return 2

    num_primes_found = 1
    n = 3

    while num_primes_found < nth_prime:
        if is_prime(n): num_primes_found += 1
        n += 2

    return n - 2


p007(10_001)
