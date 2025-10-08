import math


def is_prime(n: int) -> bool:
    """
    Returns whether a number is a prime number or not.
    :param n: The number to check.
    :return: True iff the number is a prime number, False otherwise.
    """
    return all([n % i > 0 for i in range(2, int(math.sqrt(n)) + 1)])
