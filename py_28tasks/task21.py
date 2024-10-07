from itertools import permutations


def BiggerGreater(input: str) -> str:
    perms = sorted(set(''.join(p) for p in permutations(input)))
    for perm in perms:
        if perm > input:
            return perm
    return ''
