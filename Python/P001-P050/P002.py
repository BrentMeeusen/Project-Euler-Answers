# Generate Fibonacci numbers below some value
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

# The readable approach:
fibonacci_numbers = fibonacci_numbers_with_value_below(4_000_000)
sum_of_even_fibonacci_numbers = 0

for number in fibonacci_numbers:
    if number % 2 == 0:
        sum_of_even_fibonacci_numbers += number

print(sum_of_even_fibonacci_numbers)

# Or do it all at once:
print(sum([i for i in [] if i % 2 == 0]))
