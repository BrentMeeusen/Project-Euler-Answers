# The readable approach:
from Python.timer import timer


@timer
def p001_readable() -> int:
    total = 0
    for number in range(1000):
        if number % 3 == 0 or number % 5 == 0:
            total += number
    return total

# Or, as a one-liner:
@timer
def p001_oneline() -> int:
    return sum([i for i in range(1000) if i % 3 == 0 or i % 5 == 0])

p001_readable()
p001_oneline()
