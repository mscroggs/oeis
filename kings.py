from itertools import combinations


def adjacent(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


def compute(n, neighbours, filled=[], best=None):
    if best is None:
        best = n ** 2

    if len(filled) >= best:
        return best

    # Skip some solutions that are the same but with x and y flipped
    if (0, 1) in filled and (1, 0) not in filled:
        return best

    # Skip solutions with inefficient placement around edges
    if n > 2:
        for i in range(n):
            if (0, i) in filled and (1, i) not in filled:
                return best
            if (n - 1, i) in filled and (n - 2, i) not in filled:
                return best
            if (i, 0) in filled and (i, 1) not in filled:
                return best
            if (i, n - 1) in filled and (i, n - 2) not in filled:
                return best

    # Skip solutions where pieces placed so far leave too much to do
    needed = 0
    for i in range(1, n, 3):
        for j in range(1, n, 3):
            needed += max(0, neighbours - len([p for p in filled if adjacent(p, (i, j))]))
    if len(filled) + needed >= best:
        return best
    needed = 0
    for i in range(2, n, 3):
        for j in range(2, n, 3):
            needed += max(0, neighbours - len([p for p in filled if adjacent(p, (i, j))]))
    if len(filled) + needed >= best:
        return best

    # Put three pieces next to (3a, 3b) for all a, b
    for i in range(0, n, 3):
        for j in range(0, n, 3):
            if len([p for p in filled if adjacent(p, (i, j))]) == 0:
                options = [
                    (x, y)
                    for x in range(max(0, i - 1), min(n, i + 2))
                    for y in range(max(0, j - 1), min(n, j + 2))
                ]
                for pieces in combinations(options, neighbours):
                    best = min(best, compute(
                        n, neighbours, filled + list(pieces), best
                    ))
                return best

    # Put a piece next to anywhere that has less than two pieces next to it
    for i in range(n):
        for j in range(n):
            if len([p for p in filled if adjacent(p, (i, j))]) < neighbours:
                options = [
                    (x, y)
                    for x in range(max(0, i - 1), min(n, i + 2))
                    for y in range(max(0, j - 1), min(n, j + 2))
                ]
                for p in options:
                    if p not in filled:
                        best = min(best, compute(
                            n, neighbours, filled + [p], best
                        ))
                return best

    best = min(best, len(filled))
    return best
