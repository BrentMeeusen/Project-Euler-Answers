from Python.timer import timer


@timer
def p029(max_val: int) -> int:
    powers = set()

    for a in range(2, max_val + 1):
        for b in range(2, max_val + 1):
            powers.add(a ** b)
            powers.add(b ** a)

    return len(powers)


p029(100)
