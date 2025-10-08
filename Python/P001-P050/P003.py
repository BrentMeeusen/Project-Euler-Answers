from Python.helpers import is_prime
from Python.timer import timer


@timer
def p003() -> int:
    largest_prime_factor_of = 600_851_475_143

    while not is_prime(largest_prime_factor_of):
        for i in range(3, largest_prime_factor_of, 2):
            if largest_prime_factor_of % i == 0:
                largest_prime_factor_of = largest_prime_factor_of // i
                break

    return largest_prime_factor_of

p003()
