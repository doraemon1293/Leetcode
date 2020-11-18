class Solution:
    def countVowelStrings(self, n: int) -> int:
        def f(n, k):
            if k == 1:
                return 1
            res = 0
            for i in range(n + 1):
                res += f(n - i, k - 1)
            return res

        return f(n, 5)


n = 33
print(Solution().countVowelStrings(n))
#another solution comb(n+4,4)