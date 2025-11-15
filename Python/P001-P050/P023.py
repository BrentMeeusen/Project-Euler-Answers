from Python.helpers import find_proper_divisors_of_n
from Python.timer import timer


def is_abundant(n: int) -> bool:
    return sum(find_proper_divisors_of_n(n)) > n


@timer
def p023(limit: int = 28_124) -> int:
    abundant_numbers = []

    # Find all abundant numbers until the limit
    for i in range(1, limit):
        if is_abundant(i):
            abundant_numbers.append(i)

    # Find the sums of all abundant numbers
    is_sum_of_abundant_numbers = [False] * limit
    for a in abundant_numbers:
        for b in abundant_numbers:
            if a + b < limit:
                is_sum_of_abundant_numbers[a + b] = True

    return sum(i for i, i_is_abundant in enumerate(is_sum_of_abundant_numbers) if not i_is_abundant)


p023()
