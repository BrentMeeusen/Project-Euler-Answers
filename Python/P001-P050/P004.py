from Python.timer import timer


@timer
def p004_filter() -> int:
    multiplications = [i * j for i in range(100, 1000) for j in range(100, 1000)]
    palindrome_multiplications = [n for n in multiplications if str(n) == str(n)[::-1]]
    return max(palindrome_multiplications)

@timer
def p004_sort() -> int:
    multiplications = sorted([i * j for i in range(100, 1000) for j in range(100, 1000)], reverse=True)
    for n in multiplications:
        if str(n) == str(n)[::-1]:
            return n
    return -1

@timer
def p004_oneline() -> int:
    return max([n for n in [i * j for i in range(100, 1000) for j in range(100, 1000)] if str(n) == str(n)[::-1]])

p004_filter()
p004_sort()
p004_oneline()
