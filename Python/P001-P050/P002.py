# Generate Fibonacci numbers below some value
from Python.timer import timer


def fibonacci_numbers_with_value_below(n: int) -> list[int]:
    """
    Returns all the numbers in the Fibonacci sequence that are below n.
    :param n: the max value
    :return: The list of numbers
    """
    numbers: list[int] = [0, 1]

    while numbers[-1] < n:
        numbers.append(numbers[-1] + numbers[-2])

    return numbers


@timer
def p002_readable() -> int:
    fibonacci_numbers = fibonacci_numbers_with_value_below(4_000_000)
    sum_of_even_fibonacci_numbers = 0

    for number in fibonacci_numbers:
        if number % 2 == 0:
            sum_of_even_fibonacci_numbers += number

    return sum_of_even_fibonacci_numbers

@timer
def p002_oneline() -> int:
    return sum([i for i in fibonacci_numbers_with_value_below(4_000_000) if i % 2 == 0])

p002_readable()
p002_oneline()
