from Python.timer import timer


def d(n: int) -> int:
    divisors: list[int] = [1]

    x = 2
    while x * x <= n:
        if n % x == 0:
            divisors.append(x)
            if x * x != n:
                divisors.append(n // x)
        x += 1

    return sum(divisors)


@timer
def p021(limit: int = 10_000) -> int:
    amicable_sum = 0
    for a in range(1, limit + 1):
        b = d(a)
        if d(b) == a and a != b:
            amicable_sum += a

    return amicable_sum


p021()
