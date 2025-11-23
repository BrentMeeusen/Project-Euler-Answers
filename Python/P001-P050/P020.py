from Python.helpers import str_add
from Python.timer import timer


@timer
def p020(factorial: int = 5) -> int:
    current_num = "1"

    for i in range(2, factorial + 1):
        next_num = current_num

        # Do -1 because we already have times 1 by having current_num
        for j in range(i - 1):
            next_num = str_add(next_num, current_num)

        current_num = next_num

    return sum(map(int, current_num))


p020(100)
