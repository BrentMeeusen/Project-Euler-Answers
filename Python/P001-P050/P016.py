from Python.timer import timer


def add(a: str, b: str) -> str:
    ab_sum = ""
    carry = 0
    for i in range(len(a)):
        col_sum = int(a[-i - 1]) + int(b[-i - 1]) + carry
        ab_sum = str(col_sum % 10) + ab_sum
        carry = col_sum // 10

    return ("" if carry == 0 else str(carry)) + ab_sum


@timer
def p016(power: int = 5) -> int:
    current_num = "1"

    for i in range(power):
        current_num = add(current_num, current_num)

    return sum(map(int, current_num))


p016(1000)
