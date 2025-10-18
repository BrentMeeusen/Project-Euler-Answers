import math


def is_prime(n: int) -> bool:
    """
    Returns whether a number is a prime number or not.
    :param n: The number to check.
    :return: True iff the number is a prime number, False otherwise.
    """
    return all([n % i > 0 for i in range(2, int(math.sqrt(n)) + 1)])


def find_first_n_primes(n: int) -> list[int]:
    """
    Returns a list of the first `n` prime numbers.
    :param n: The number of primes to find.
    :return: The list of primes.
    """
    if n == 0:
        return []
    elif n == 1:
        return [2]

    primes = [2]
    x = 3
    while len(primes) < n:
        if is_prime(x):
            primes.append(x)
        x += 2

    return primes
