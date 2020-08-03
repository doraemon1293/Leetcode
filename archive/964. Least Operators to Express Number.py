class Solution(object):
    def leastOpsExpressTarget(self, x, target):
        memo = {}

        def dp(i, targ):
            if (i, targ) in memo:
                return memo[i, targ]
            if targ == 0: return 0
            if targ == 1: return 2 if i == 0 else i
            if i >= 39: return float('inf')

            t, r = divmod(targ, x)
            memo[i,targ]= min(r * (2 if i == 0 else i) + dp(i + 1, t),(x - r) * (2 if i == 0 else i) + dp(i + 1, t + 1))
            return memo[i,targ]

        return dp(0, target) - 1
