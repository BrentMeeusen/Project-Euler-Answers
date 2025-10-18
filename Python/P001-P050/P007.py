from Python.helpers import is_prime, find_first_n_primes
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


@timer
def p007_helper(nth_prime: int) -> int:
    return find_first_n_primes(nth_prime)[-1]


p007(10_001)
p007_helper(10_001)
