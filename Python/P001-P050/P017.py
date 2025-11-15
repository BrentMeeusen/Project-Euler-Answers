from Python.timer import timer


def get_number_length(num: int) -> int:
    # Even though "zero" has 4 letters, we assume it has 0, as 130 is not written as "one hundred and thirty zero".
    # Since we don't have to include 0 anyway (the range is [1, 1000]), this will not cause further problems.
    #                 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19
    number_lengths = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    differing_abstract_lengths = {
        20: 4,
        30: 4,
        40: 3,
        50: 3,
        80: 4,
    }
    number_length = 0

    # 0-20
    if num < len(number_lengths):
        return number_lengths[num]

    # 1000
    elif num == 1000:
        return len("onethousand")

    # 100s
    hundredths = num // 100
    if hundredths > 0:
        number_length += number_lengths[hundredths] + 7

    num -= hundredths * 100

    # Return if nothing else is after 100s
    if num == 0:
        return number_length

    # Return sum for "X hundred *and Y*" if Y is between [1-19]
    if num <= 19:
        return number_length + 3 + number_lengths[num]

    # Add "and" to all other cases if there's 100s
    if hundredths > 0:
        number_length += 3

    # 10s
    tenths = num // 10
    if tenths > 0:
        number_length += differing_abstract_lengths.get(tenths * 10, number_lengths[tenths]) + 2

    num -= tenths * 10

    # 1s
    return number_length + number_lengths[num]


@timer
def p017(limit: int = 5) -> int:
    return sum([get_number_length(n) for n in range(1, limit + 1)])


p017(1000)
