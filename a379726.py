"""Python code to compute A379726."""


def adjacent(a, b):
    return abs(a[0] - b[0]) <= 1 and abs(a[1] - b[1]) <= 1


def compute(n, filled=[], best=None):
    if best is None:
        best = n ** 2

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

    if len(filled) >= best:
        return best

    for i in range(0, n, 3):
        for j in range(0, n, 3):
            if len([p for p in filled if adjacent(p, (i, j))]) == 0:
                xr = (max(0, i - 1), min(n, i + 2))
                yr = (max(0, j - 1), min(n, j + 2))
                for x in range(*xr):
                    for y in range(*yr):
                        if (x, y) in filled:
                            continue
                        for x2 in range(*xr):
                            for y2 in range(*yr):
                                if (x2, y2) <= (x, y):
                                    continue
                                if (x2, y2) in filled:
                                    continue
                                best = min(best, compute(
                                    n, filled + [(x, y), (x2, y2)], best
                                ))
                return best

    for i in range(n):
        for j in range(n):
            xr = (max(0, i - 1), min(n, i + 2))
            yr = (max(0, j - 1), min(n, j + 2))
            if len([p for p in filled if adjacent(p, (i, j))]) < 2:
                for x in range(*xr):
                    for y in range(*yr):
                        if (x, y) not in filled:
                            best = min(best, compute(
                                n, filled + [(x, y)], best
                            ))
                return best

    best = min(best, len(filled))
    return best


print("Checking 2")
assert compute(2) == 2
print("Checking 3")
assert compute(3) == 3
print("Checking 4")
assert compute(4) == 8

for n in range(2, 12):
    if n % 3 == 0:
        term = compute(n, best=2 * (n//3)**2 + n//3)
        print(f"{n} {term}")
    else:
        print(f"{n} {2 * (n//3)**2}")
