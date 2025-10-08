from Python.timer import timer


@timer
def p005_intuitive(i: int = 20) -> int:
    n = i
    ints_from_1_to_i = range(2, i + 1)
    while True:
        if all(map(lambda x: n % x == 0, ints_from_1_to_i)):
            return n

        n += i

@timer
def p005_quicker(i: int = 20) -> int:
    n = i
    ints_from_1_to_i = range(2, i + 1)

    while True:
        is_evenly_divisible_by_1_to_i = True
        for x in ints_from_1_to_i:
            if n % x > 0:
                is_evenly_divisible_by_1_to_i = False
                n += i
                break

        if is_evenly_divisible_by_1_to_i:
            return n

@timer
def p005_quickest(i: int = 20) -> int:
    v = 1

    for x in range(2, i + 1):
        if v % x > 0:
            for y in range(2, i + 1):
                if (v * y) % x == 0:
                    v *= y
                    break

    return v

# p005_intuitive()
# p005_quicker()
p005_quickest()
