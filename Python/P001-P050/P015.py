from Python.timer import timer


def factorial(n):
    x = 1
    while n > 1:
        x *= n
        n -= 1
    return x


@timer
def p015_computational(grid_size: int) -> int:
    # To represent `n` lines, we need `n + 1` nodes
    grid_size += 1

    # Create empty grid
    grid = [[0 for _ in range(grid_size)] for _ in range(grid_size)]

    # Put 1s in the first row and column
    grid[0] = [1 for _ in range(grid_size)]
    for i in range(grid_size):
        grid[i][0] = 1

    # Compute the rest
    for row in range(0, grid_size):
        for col in range(row, grid_size):
            grid[row][col] = grid[row][col - 1] + (0 if row == 0 else grid[row - 1][col])
            grid[col][row] = grid[row][col]

    return grid[grid_size - 1][grid_size - 1]


@timer
def p015_math(grid_size: int) -> int:
    return int(factorial(grid_size * 2) / (factorial(grid_size) ** 2))


p015_computational(20)
p015_math(20)
