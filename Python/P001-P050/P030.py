from Python.timer import timer


def sum_power(n: int, power: int) -> int:
    return sum([int(i) ** power for i in str(n)])


@timer
def p030(num_digits: int) -> int:
    sum_powers = []

    for n in range(10, (9 ** num_digits) * num_digits + 1):
        if n == sum_power(n, num_digits):
            print(f"Adding {n}")
            sum_powers.append(n)

    return sum(sum_powers)


p030(5)
