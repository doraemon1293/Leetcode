class Solution:
    def fib(self, N):
        """
        :type N: int
        :rtype: int
        """
        a, b = 0, 1
        if N == 0:
            return a
        if N == 1:
            return b
        N -= 1
        while N > 0:
            a, b = b, a + b
            N -= 1
        return b


print(Solution().fib(5))
