import math


def is_prime(n: int) -> bool:
    """
    Returns whether a number is a prime number or not.
    :param n: The number to check.
    :return: True iff the number is a prime number, False otherwise.
    """
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True


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


def find_primes_below_n(n: int) -> list[int]:
    """
    Returns a list of the primes below `n`.
    :param n: The maximum value of `n`.
    :return: The list of primes.
    """
    # Using the sieve of Eratosthenes
    primes = [True for _ in range(n)]

    x = 2
    while x ** 2 < n:
        if primes[x] == True:
            for i in range(x ** 2, n, x):
                primes[i] = False
        x += 1

    return [i for i in range(2, n) if primes[i] == True]

    # My initial, intuitive approach
    # if n <= 2:
    #     return []
    #
    # primes = [2]
    # for x in range(3, n, 2):
    #     if is_prime(x):
    #         primes.append(x)
    #
    # return primes


def find_proper_divisors_of_n(n: int) -> list[int]:
    """
    Returns a list of the divisors of `n`, excluding `n`.
    :param n: The number to find the divisors of.
    :return: The list of divisors.
    """
    divisors: list[int] = [1]

    x = 2
    while x * x <= n:
        if n % x == 0:
            divisors.append(x)
            if x * x != n:
                divisors.append(n // x)
        x += 1

    return divisors
