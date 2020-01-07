class Solution:
    def circularPermutation(self, n: int, start: int) -> list:
        code = ["0", "1"]
        for _ in range(n-1):
            code = ["0" + x for x in code] + ["1" + x for x in code[::-1]]
        code=[int(x,2) for x in code]
        return code[code.index(start):]+code[:code.index(start)]


n = 3
start = 2
print(Solution().circularPermutation(n, start))
