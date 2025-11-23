from Python.timer import timer


def compute_cycle_length(n: int) -> int:
    seen = {}

    x = 1
    i = 0
    while True:
        if x in seen:
            return i - seen[x]
        else:
            seen[x] = i
            x = (x * 10) % n
            i += 1


@timer
def p026() -> int:
    nums = [compute_cycle_length(n) for n in range(1, 1000)]
    return nums.index(max(nums)) + 1


p026()
