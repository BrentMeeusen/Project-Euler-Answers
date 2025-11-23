from Python.helpers import str_add
from Python.timer import timer


@timer
def p025(num_length: int = 3) -> int:
    a = "1"
    b = "1"

    index = 2
    while len(b) < num_length:
        tmp = b
        b = str_add(b, a)
        a = tmp

        index += 1

    return index


p025(1000)
