from Python.timer import timer


def rotate_cw(direction: tuple[int, int]) -> tuple[int, int]:
    if direction == (1, 0):
        return 0, -1
    elif direction == (0, -1):
        return -1, 0
    elif direction == (-1, 0):
        return 0, 1
    else:
        return 1, 0


@timer
def p028(spiral_size: int) -> int:
    x = y = spiral_size // 2 + 1

    diagonal_sum = 1
    direction = (0, -1)

    x += 1
    curr_n = 2

    while x < spiral_size + 1 and y < spiral_size + 1:

        # If we're in the top left corner, move one more step right before rotating clockwise
        force_rotate = False
        if x == y and x > spiral_size // 2:
            force_rotate = True

        # If we're in any other corner, rotate clockwise
        if force_rotate or x == y or x == (spiral_size - y + 1) or (spiral_size - x + 1) == y:
            diagonal_sum += curr_n
            direction = rotate_cw(direction)

        if force_rotate:
            x += 1
            curr_n += 1

        curr_n += 1
        x += direction[0]
        y += direction[1]

    return diagonal_sum


p028(1001)
