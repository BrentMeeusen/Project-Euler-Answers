from Python.timer import timer


@timer
def p009():
    for a in range(1, 999):
        for b in range(a + 1, 999):
            c = 1000 - b - a
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c

    return 0


p009()
