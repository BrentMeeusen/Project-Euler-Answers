from Python.timer import timer


def compute_permutations(permutate: list) -> list:
    permutations = []

    if len(permutate) == 2:
        permutations.extend((permutate[0] + permutate[1], permutate[1] + permutate[0]))
        return permutations

    for p in permutate:
        permutates_without_p = permutate.copy()
        permutates_without_p.remove(p)

        permutations.extend([p + permutation for permutation in compute_permutations(permutates_without_p)])

    return permutations


@timer
def p024(permutate: list, nth_permutation=1) -> list:
    permutations = compute_permutations(permutate)
    return permutations[nth_permutation - 1]


p024([str(n) for n in range(10)], 1_000_000)
