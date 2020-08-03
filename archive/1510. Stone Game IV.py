class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        n2 = []
        for i in range(1, 1000):
            if i ** 2 > n:
                break
            n2.append(i ** 2)
        n2_set = set(n2)
        memo = {}

        def f(n):
            if n in n2_set:
                return True
            if n in memo:
                return memo[n]
            for i in n2:
                if i > n:
                    break
                if not (f(n - i)):
                    memo[n] = True
                    return True
            memo[n] = False
            return False

        return f(n)


print(Solution().winnerSquareGame(17))
