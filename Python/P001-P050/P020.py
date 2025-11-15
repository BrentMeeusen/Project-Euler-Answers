from Python.timer import timer


def add(a: str, b: str) -> str:
    ab_sum = ""
    carry = 0

    if len(b) < len(a):
        b = "0" * (len(a) - len(b)) + b

    for i in range(len(a)):
        col_sum = int(a[-i - 1]) + int(b[-i - 1]) + carry
        ab_sum = str(col_sum % 10) + ab_sum
        carry = col_sum // 10

    return ("" if carry == 0 else str(carry)) + ab_sum


@timer
def p020(factorial: int = 5) -> int:
    current_num = "1"

    for i in range(2, factorial + 1):
        next_num = current_num

        # Do -1 because we already have times 1 by having current_num
        for j in range(i - 1):
            next_num = add(next_num, current_num)

        current_num = next_num

    return sum(map(int, current_num))


p020(100)
