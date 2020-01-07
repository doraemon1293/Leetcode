def gen(m, n):
    # pick n from m choices

    if n == 0:
        yield []
    st, end = m
    for i in range(st, end):
        for res in gen((i + 1, end), n - 1):
            yield [i] + res


class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.gen = gen((0,len(characters)), combinationLength)
        self.characters=characters
        try:
            self.next_comb = next(self.gen)
        except StopIteration:
            self.next = None

    def next(self) -> str:
        res = self.next_comb
        try:
            self.next_comb = next(self.gen)
        except StopIteration:
            self.next_comb = None
        return "".join([self.characters[i] for i in res])

    def hasNext(self) -> bool:
        return self.next_comb != None


# Your CombinationIterator object will be instantiated and called as such:
obj = CombinationIterator("abc", 2)
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())
print(obj.next())
print(obj.hasNext())

