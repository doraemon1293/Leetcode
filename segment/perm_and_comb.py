def perm(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)):
        v = items[i]
        if n == 1:
            yield [v]
        else:
            rest = items[:i] + items[i + 1:]
            for p in perm(rest, n - 1):
                yield [v] + p


def comb(items, n=None):
    if n is None:
        n = len(items)
    for i in range(len(items)-n+1):
        v = items[i]
        if n == 1:
            yield [v]
        else:
            rest = items[i + 1:]
            if len(rest) >= n - 1:
                for c in comb(rest, n - 1):
                    yield [v] + c


print(list(perm([1, 2, 3, 4, 5], 2)))
print(list(comb([1, 2, 3, 4, 5], 2)))
