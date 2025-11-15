from Python.timer import timer


@timer
def p022() -> int:
    # Read the text file
    with open("./../../Data/P022.txt") as f:
        names = sorted(list(map(lambda name: name[1:-1], f.readline().split(","))))

    total_name_score = 0
    for i, name in enumerate(names):
        name_score = sum(map(lambda char: ord(char), name)) - 64 * len(name)
        total_name_score += name_score * (i + 1)

    return total_name_score


p022()
