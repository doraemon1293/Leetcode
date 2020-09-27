class Solution:
    def thousandSeparator(self, n: int) -> str:
        res = []

        for i, ch in enumerate(str(n)[::-1]):
            res.append(ch)
            if i % 3 == 2 and i != len(str(n)) - 1:
                res.append(".")
        return "".join(res[::-1])

