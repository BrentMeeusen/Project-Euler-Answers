from Python.timer import timer


@timer
def p014():
    sequence_length: dict[int, int] = {}
    max_length = 0
    max_pos = 0

    for i in range(1, 1_000_000):
        n = i

        steps = 1
        while n != 1:
            if sequence_length.get(n, None) is not None:
                steps += sequence_length[n] - 1
                break

            if n % 2 == 0:
                n //= 2
            else:
                n = 3 * n + 1
            steps += 1

        sequence_length[i] = steps
        if steps > max_length:
            max_length = steps
            max_pos = i

    return max_pos


p014()
