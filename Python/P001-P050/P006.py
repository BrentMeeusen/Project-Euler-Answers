from Python.timer import timer


def sum_of_squares(nums: range) -> int:
    return sum(map(lambda x: x ** 2, nums))


def square_of_sums(nums: range) -> int:
    return sum(nums) ** 2


@timer
def p006(n: int) -> int:
    nums = range(1, n + 1)
    return square_of_sums(nums) - sum_of_squares(nums)


p006(100)
