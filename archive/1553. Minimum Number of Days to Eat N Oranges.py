class Solution:
    def minDays(self, n: int) -> int:
        memo = {0: 0, 1: 1}

        def foo(n):
            if n in memo:
                return memo[n]
            memo[n]=min(n%2+foo(n//2),n%3+foo(n//3))+1
            return memo[n]
        return foo(n)
print(
    Solution().minDays(2*(10**9))
)