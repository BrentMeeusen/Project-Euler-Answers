from Python.timer import timer


def is_leap_year(year: int) -> bool:
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


@timer
def p019() -> int:
    month_lengths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    year = 1900
    month = 0
    day_index = 0

    sundays_on_first_of_month = 0

    while year <= 2000:
        while month <= 11:
            if day_index % 7 == 6 and year >= 1901:
                sundays_on_first_of_month += 1

            day_index = (day_index + (29 if is_leap_year(year) and month == 1 else month_lengths[month])) % 7

            month += 1
        year += 1
        month = 0

    return sundays_on_first_of_month


p019()
